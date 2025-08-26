from django.db import models
from django.contrib.auth.models import User
from orders.models import Order  # assuming you have an orders app

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # e.g. Stripe, Razorpay
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=(
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ), default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"
