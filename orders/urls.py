from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("summary/", views.order_summary, name="order_summary"),
    path("place/", views.place_order, name="place_order"),
    path("success/<int:order_id>/", views.order_success, name="order_success"),
    path("history/", views.order_history, name="order_history"),
]
