from rest_framework import serializers
from .models import Badge, TrainingAttempt, UserBadge

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = "__all__"

class UserBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)
    class Meta:
        model = UserBadge
        fields = ("id", "badge", "awarded_at")

class AttemptSerializer(serializers.ModelSerializer):
    scenario_title = serializers.CharField(source="scenario.title", read_only=True)
    class Meta:
        model = TrainingAttempt
        fields = ("id", "scenario", "scenario_title", "selected_answer", "correct", "points_earned", "created_at")
