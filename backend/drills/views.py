from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    SafetyDrill,
    DrillParticipation
)

from .serializers import (
    SafetyDrillSerializer,
    DrillParticipationSerializer
)


class SafetyDrillViewSet(viewsets.ModelViewSet):

    serializer_class = SafetyDrillSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'ship',
        'drill_type',
        'scheduled_date'
    ]

    def get_queryset(self):

        return SafetyDrill.objects.all()

    def perform_create(self, serializer):

        if self.request.user.role != "ADMIN":
            raise PermissionError(
                "Only admin can schedule drills"
            )

        serializer.save(
            created_by=self.request.user
        )


class DrillParticipationViewSet(viewsets.ModelViewSet):

    serializer_class = DrillParticipationSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'status',
        'drill'
    ]

    def get_queryset(self):

        user = self.request.user

        queryset = DrillParticipation.objects.all()

        if user.role != "ADMIN":

            queryset = queryset.filter(
                crew_member=user
            )

        return queryset

    def perform_update(self, serializer):

        participation = self.get_object()

        if (
            self.request.user.role == "CREW"
            and participation.crew_member != self.request.user
        ):
            raise PermissionError(
                "Cannot update others participation"
            )

        serializer.save()