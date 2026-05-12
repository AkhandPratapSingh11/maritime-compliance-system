from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MaintenanceTask
from .serializers import MaintenanceTaskSerializer
from django.utils import timezone


class MaintenanceTaskViewSet(viewsets.ModelViewSet):

    serializer_class = MaintenanceTaskSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'ship',
        'status',
        'due_date'
    ]

    def get_queryset(self):

        user = self.request.user

        queryset = MaintenanceTask.objects.all()

        # =========================
        # RBAC
        # =========================

        if user.role != "ADMIN":

            queryset = queryset.filter(
                assigned_to=user
            )

        # =========================
        # OVERDUE FILTER
        # =========================

        overdue = self.request.query_params.get(
            'overdue'
        )

        if overdue == 'true':

            queryset = queryset.exclude(
                status="COMPLETED"
            ).filter(
                due_date__lt=timezone.now().date()
            )

        return queryset

    def perform_create(self, serializer):

        if self.request.user.role != "ADMIN":
            raise PermissionError(
                "Only admin can create tasks"
            )

        serializer.save()

    def perform_update(self, serializer):

        task = self.get_object()
        user = self.request.user

        if user.role == "CREW":

            if task.assigned_to != user:
                raise PermissionError(
                    "You can only update your own tasks"
                )

        serializer.save()