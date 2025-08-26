from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),       # Home page
    path("contact/", views.contact, name="contact"),  # Contact page
]
