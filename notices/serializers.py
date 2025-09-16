from rest_framework import serializers
from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            "id",
            "title",
            "message",
            "audience",
            "recipient",
            "created_by",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


