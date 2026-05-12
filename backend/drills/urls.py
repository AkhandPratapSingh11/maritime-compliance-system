from rest_framework.routers import DefaultRouter
from .views import (
    SafetyDrillViewSet,
    DrillParticipationViewSet
)

router = DefaultRouter()

router.register(
    r'drills',
    SafetyDrillViewSet,
    basename='drills'
)

router.register(
    r'participation',
    DrillParticipationViewSet,
    basename='participation'
)

urlpatterns = router.urls