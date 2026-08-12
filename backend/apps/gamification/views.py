from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Badge, TrainingAttempt, UserBadge
from .serializers import BadgeSerializer, AttemptSerializer, UserBadgeSerializer

class MyAttemptsView(generics.ListAPIView):
    serializer_class = AttemptSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return TrainingAttempt.objects.filter(user=self.request.user).select_related("scenario").order_by("-created_at")[:50]

class MyBadgesView(generics.ListAPIView):
    serializer_class = UserBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return UserBadge.objects.filter(user=self.request.user).select_related("badge").order_by("-awarded_at")

class BadgeListView(generics.ListAPIView):
    queryset = Badge.objects.all().order_by("required_points")
    serializer_class = BadgeSerializer
    permission_classes = [permissions.AllowAny]

class LeaderboardView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        users = User.objects.filter(is_active=True).select_related("profile").order_by("-profile__points", "username")[:20]
        rows = []
        for i, user in enumerate(users, 1):
            if hasattr(user, "profile"):
                rows.append({
                    "rank": i, "username": user.username,
                    "points": user.profile.points, "level": user.profile.level
                })
        return Response(rows)
