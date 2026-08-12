from django.db import transaction
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Scenario
from .permissions import IsAdminRole
from .serializers import ScenarioSerializer
from apps.accounts.models import UserProfile
from apps.gamification.models import Badge, TrainingAttempt, UserBadge
from apps.notifications.models import Notification

class ScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            return Scenario.objects.filter(active=True).order_by("-created_at")
        return Scenario.objects.all().order_by("-created_at")

    def get_permissions(self):
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            return [permissions.AllowAny()]
        return [IsAdminRole()]

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def submit_attempt(request):
    scenario_id = request.data.get("scenario_id")
    answer = request.data.get("answer")

    try:
        scenario = Scenario.objects.get(pk=scenario_id, active=True)
    except Scenario.DoesNotExist:
        return Response({"detail": "Scenario not found."}, status=status.HTTP_404_NOT_FOUND)

    content = scenario.content or {}
    correct_answer = content.get("correct_answer")
    correct = answer == correct_answer
    earned = scenario.points if correct else 0

    attempt = TrainingAttempt.objects.create(
        user=request.user,
        scenario=scenario,
        selected_answer=str(answer or ""),
        correct=correct,
        points_earned=earned,
    )

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    profile.points += earned
    profile.refresh_level()
    today = timezone.localdate()
    if profile.last_training_date != today:
        if profile.last_training_date and (today - profile.last_training_date).days == 1:
            profile.training_streak += 1
        else:
            profile.training_streak = 1
        profile.last_training_date = today
    profile.save()

    awarded = []
    for badge in Badge.objects.filter(required_points__lte=profile.points):
        _, created = UserBadge.objects.get_or_create(user=request.user, badge=badge)
        if created:
            awarded.append({"name": badge.name, "icon": badge.icon})
            Notification.objects.create(
                user=request.user,
                title="New badge unlocked",
                message=f"You earned the {badge.name} badge."
            )

    return Response({
        "correct": correct,
        "earned_points": earned,
        "total_points": profile.points,
        "level": profile.level,
        "streak": profile.training_streak,
        "explanation": content.get("explanation", "Review the security indicators in this scenario."),
        "feedback": "Excellent decision." if correct else "Review the indicators and try again.",
        "badges_awarded": awarded,
        "attempt_id": attempt.id,
    })
