from django.db import models
from django.conf import settings


class Payment(models.Model):
    class Method(models.TextChoices):
        cash = "cash", "Cash"
        mpesa = "mpesa", "M-Pesa"
        bank = "bank", "Bank"

    class Status(models.TextChoices):
        pending = "pending", "Pending"
        completed = "completed", "Completed"
        failed = "failed", "Failed"

    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments")
    unit = models.ForeignKey("apartments.Unit", on_delete=models.PROTECT, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.pending)
    reference = models.CharField(max_length=100, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Payment {self.id} - {self.tenant} - {self.amount}"

