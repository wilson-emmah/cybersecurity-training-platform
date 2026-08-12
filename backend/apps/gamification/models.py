from django.contrib.auth.models import User
from django.db import models

class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=20, default="🏆")
    required_points = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "badge")

class TrainingAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="training_attempts")
    scenario = models.ForeignKey("scenarios.Scenario", on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    points_earned = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="training_notifications")
    title = models.CharField(max_length=150)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
