from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "current_category": category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "products/product_detail.html", {"product": product})


def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})
