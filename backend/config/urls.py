from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # Apps
    path('api/', include('ships.urls')),
    path('api/', include('maintenance.urls')),
    path('api/', include('drills.urls')),
    path('api/', include('dashboard.urls')),
]