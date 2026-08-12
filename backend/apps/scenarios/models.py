from django.db import models

class Scenario(models.Model):
    CATEGORY_CHOICES = [
        ("phishing", "Phishing"),
        ("url", "Suspicious URL"),
        ("password", "Password Security"),
        ("malware", "Malware Awareness"),
        ("social", "Social Engineering"),
    ]
    DIFFICULTY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=30, choices=DIFFICULTY_CHOICES, default="beginner")
    description = models.TextField()
    content = models.JSONField(default=dict)
    points = models.PositiveIntegerField(default=10)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
