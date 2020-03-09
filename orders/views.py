from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from cart.models import Cart
from .models import Order
from django.contrib.auth.decorators import login_required
from .utils import id_generator
from .forms import CheckoutForm


@login_required
def orders(request):
    empty_message = "You have no orders to see"
    empty = False
    if request.user.cart_user.filter(active=False).count() <= 0:
        empty = True
    context = {
        'empty': empty,
        'empty_message': empty_message,
        'cart_list': request.user.cart_user.filter(active=False),
    }
    template = "orders/user.html"
    return render(request, template, context)


@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user, active=True)
    except:
        return HttpResponseRedirect(reverse("cart"))
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse("cart"))

    new_order.total = float(new_order.shipping_total) + float(cart.total)
    new_order.save()
    if new_order.status == "Finished":
        cart.active = False
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))
    if not request.user.addresses.all():
        return redirect('new_address')
    context = {
        'user': request.user,
        'cart': cart,
    }
    template = "orders/checkout.html"
    return render(request, template, context)
