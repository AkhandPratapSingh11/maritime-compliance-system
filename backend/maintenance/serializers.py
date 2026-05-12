from rest_framework import serializers
from .models import MaintenanceTask


class MaintenanceTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceTask
        fields = "__all__"