from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Payment
from orders.models import Order
import uuid

def process_payment(request, order_id):
    """
    Mock payment processing.
    Replace with Razorpay/Stripe/PayPal API integration.
    """
    try:
        order = Order.objects.get(id=order_id, user=request.user)
        transaction_id = str(uuid.uuid4())[:12]

        # create payment entry
        payment = Payment.objects.create(
            order=order,
            user=request.user,
            amount=order.total_price,
            payment_method="MockGateway",
            transaction_id=transaction_id,
            status="completed",
        )

        order.is_paid = True
        order.save()

        messages.success(request, "Payment successful!")
        return redirect("payments:payment_success")

    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect("core:home")


def payment_success(request):
    return render(request, "payments/payment_success.html")
