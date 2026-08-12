from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ScenarioViewSet, submit_attempt

router = DefaultRouter()
router.register("", ScenarioViewSet, basename="scenario")

urlpatterns = [
    path("submit/", submit_attempt),
    path("", include(router.urls)),
]
