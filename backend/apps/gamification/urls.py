from django.urls import path
from .views import MyAttemptsView, MyBadgesView, BadgeListView, LeaderboardView

urlpatterns = [
    path("attempts/", MyAttemptsView.as_view()),
    path("my-badges/", MyBadgesView.as_view()),
    path("badges/", BadgeListView.as_view()),
    path("leaderboard/", LeaderboardView.as_view()),
]
