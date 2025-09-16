from django.db import models
from django.conf import settings


class Notice(models.Model):
    class Audience(models.TextChoices):
        all = "all", "All Users"
        landlords = "landlords", "Landlords"
        caretakers = "caretakers", "Caretakers"
        tenants = "tenants", "Tenants"

    title = models.CharField(max_length=255)
    message = models.TextField()
    audience = models.CharField(max_length=20, choices=Audience.choices, default=Audience.tenants)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="notices"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_notices"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

