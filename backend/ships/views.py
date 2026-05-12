from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsAdminUserRole

from .models import Ship
from .serializers import ShipSerializer


class ShipViewSet(viewsets.ModelViewSet):

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole
    ]