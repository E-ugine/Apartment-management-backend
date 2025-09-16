from rest_framework import serializers
from .models import MaintenanceRequest


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = (
            "id",
            "unit",
            "created_by",
            "assigned_to",
            "description",
            "status",
            "priority",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


