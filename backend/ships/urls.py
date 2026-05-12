from rest_framework.routers import DefaultRouter
from .views import ShipViewSet

router = DefaultRouter()
router.register(r'ships', ShipViewSet)

urlpatterns = router.urls