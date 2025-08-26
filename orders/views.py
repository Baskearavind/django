from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem

@login_required
def order_summary(request):
    """Show items from cart before placing order"""
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.get_subtotal() for item in items)

    return render(request, "orders/order_summary.html", {"items": items, "total": total})


@login_required
def place_order(request):
    """Convert cart into order"""
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)

    if not items:
        messages.error(request, "Your cart is empty.")
        return redirect("cart:cart_detail")

    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
        total_price += item.get_subtotal()

    order.total_price = total_price
    order.save()

    # clear cart
    items.delete()
    cart.save()

    messages.success(request, "Order placed! Please proceed to payment.")
    return redirect("orders:order_success", order_id=order.id)


@login_required
def order_success(request, order_id):
    """After placing order (before or after payment)"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})


@login_required
def order_history(request):
    """Show all past orders"""
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_history.html", {"orders": orders})
