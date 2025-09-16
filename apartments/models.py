from django.db import models
from django.conf import settings


class Unit(models.Model):
    apartment_name = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=50)
    floor = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_occupied = models.BooleanField(default=False)
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="units",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("apartment_name", "unit_number")
        ordering = ["apartment_name", "unit_number"]

    def __str__(self):
        return f"{self.apartment_name} - {self.unit_number}"

