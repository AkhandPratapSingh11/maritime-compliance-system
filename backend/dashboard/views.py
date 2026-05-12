from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from maintenance.models import MaintenanceTask
from drills.models import DrillParticipation


class ComplianceDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        today = timezone.now().date()

        user = request.user

        # =========================
        # FILTER DATA
        # =========================

        if user.role == "ADMIN":

            maintenance_tasks = MaintenanceTask.objects.all()

            drill_participation = (
                DrillParticipation.objects.all()
            )

        else:

            maintenance_tasks = (
                MaintenanceTask.objects.filter(
                    assigned_to=user
                )
            )

            drill_participation = (
                DrillParticipation.objects.filter(
                    crew_member=user
                )
            )

        # =========================
        # MAINTENANCE COUNTS
        # =========================

        total_tasks = maintenance_tasks.count()

        completed_tasks = (
            maintenance_tasks.filter(
                status="COMPLETED"
            ).count()
        )

        pending_tasks = (
            maintenance_tasks.exclude(
                status="COMPLETED"
            ).count()
        )

        overdue_tasks = (
            maintenance_tasks.exclude(
                status="COMPLETED"
            ).filter(
                due_date__lt=today
            ).count()
        )

        # =========================
        # DRILL COUNTS
        # =========================

        total_drills = (
            drill_participation.count()
        )

        attended_drills = (
            drill_participation.filter(
                status="ATTENDED"
            ).count()
        )

        missed_drills = (
            drill_participation.exclude(
                status="ATTENDED"
            ).filter(
                drill__scheduled_date__lt=today
            ).count()
        )

        # =========================
        # COMPLIANCE %
        # =========================

        maintenance_compliance = 0

        if total_tasks > 0:
            maintenance_compliance = round(
                (completed_tasks / total_tasks) * 100,
                2
            )

        drill_compliance = 0

        if total_drills > 0:
            drill_compliance = round(
                (attended_drills / total_drills) * 100,
                2
            )

        overall_compliance = round(
            (
                maintenance_compliance
                + drill_compliance
            ) / 2,
            2
        )

        # =========================
        # RESPONSE
        # =========================

        return Response({

            "maintenance": {
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "pending_tasks": pending_tasks,
                "overdue_tasks": overdue_tasks,
                "compliance_percentage":
                    maintenance_compliance
            },

            "drills": {
                "total_drills": total_drills,
                "attended_drills":
                    attended_drills,
                "missed_drills":
                    missed_drills,
                "compliance_percentage":
                    drill_compliance
            },

            "overall_compliance":
                overall_compliance
        })