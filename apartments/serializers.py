from rest_framework import serializers
from .models import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
            "id",
            "apartment_name",
            "unit_number",
            "floor",
            "bedrooms",
            "bathrooms",
            "rent_amount",
            "is_occupied",
            "tenant",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


