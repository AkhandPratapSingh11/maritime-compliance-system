from rest_framework import serializers
from .models import SafetyDrill, DrillParticipation


class SafetyDrillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafetyDrill
        fields = "__all__"


class DrillParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrillParticipation
        fields = "__all__"