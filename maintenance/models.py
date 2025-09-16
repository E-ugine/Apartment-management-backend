from django.db import models
from django.conf import settings


class MaintenanceRequest(models.Model):
    class Status(models.TextChoices):
        open = "open", "Open"
        in_progress = "in_progress", "In Progress"
        resolved = "resolved", "Resolved"
        closed = "closed", "Closed"

    class Priority(models.TextChoices):
        low = "low", "Low"
        medium = "medium", "Medium"
        high = "high", "High"

    unit = models.ForeignKey("apartments.Unit", on_delete=models.CASCADE, related_name="maintenance_requests")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="maintenance_requests")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_maintenance"
    )
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.open)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.medium)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.unit} - {self.status}"

