from django.urls import path

from .views import ComplianceDashboardView


urlpatterns = [
    path(
        'dashboard/',
        ComplianceDashboardView.as_view()
    ),
]