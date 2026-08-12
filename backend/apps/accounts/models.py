from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = (("student", "Student"), ("admin", "Admin"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    points = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    training_streak = models.PositiveIntegerField(default=0)
    last_training_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def refresh_level(self):
        self.level = max(1, (self.points // 100) + 1)
