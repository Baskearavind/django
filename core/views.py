from django.shortcuts import render

def index(request):
    # Home page view
    return render(request, "core/index.html")

def contact(request):
    # Contact page view
    return render(request, "core/contact.html")
