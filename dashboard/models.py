from django.db import models
from django.contrib.auth.models import User


class Shipment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipments")
    provider = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_shipments")

    # Step 1: Pickup Details
    pickup_address = models.CharField(max_length=255)
    pickup_city = models.CharField(max_length=100)
    pickup_state = models.CharField(max_length=100)

    # Step 2: Dropoff Details
    dropoff_address = models.CharField(max_length=255)
    dropoff_city = models.CharField(max_length=100)
    dropoff_state = models.CharField(max_length=100)

    # Step 3: Package Details
    package_description = models.TextField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    dimensions = models.CharField(max_length=100, help_text="Format: LxWxH cm")

    # Step 4: Payment / Tracking
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    tracking_number = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipment {self.tracking_number} - {self.customer.username}"
