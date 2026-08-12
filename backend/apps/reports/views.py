from django.contrib.auth.models import User
from django.db.models import Avg, Count, Sum
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.models import UserProfile
from apps.gamification.models import TrainingAttempt
from apps.scenarios.models import Scenario

class AdminOverviewView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        attempts = TrainingAttempt.objects.all()
        return Response({
            "users": User.objects.count(),
            "scenarios": Scenario.objects.count(),
            "attempts": attempts.count(),
            "correct_attempts": attempts.filter(correct=True).count(),
            "average_score": attempts.aggregate(avg=Avg("points_earned"))["avg"] or 0,
            "total_points_awarded": attempts.aggregate(total=Sum("points_earned"))["total"] or 0,
        })
