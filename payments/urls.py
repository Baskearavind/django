from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("process/<int:order_id>/", views.process_payment, name="process_payment"),
    path("success/", views.payment_success, name="payment_success"),
]
