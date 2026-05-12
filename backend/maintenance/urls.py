from rest_framework.routers import DefaultRouter
from .views import MaintenanceTaskViewSet

router = DefaultRouter()
router.register(
    r'maintenance',
    MaintenanceTaskViewSet,
    basename='maintenance'
)
urlpatterns = router.urls