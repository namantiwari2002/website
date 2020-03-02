from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from blog.models import Product, Variation
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def cart_home(request):
    cart = Cart.objects.filter(user=request.user, active=True).first()
    empty_message = "Your cart is Empty, please keep shopping."
    if cart is not None:
        context = {"cart": cart, "empty": False}
        new_total = 0.00
        for item in cart.cart_item.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        cart.total = new_total
        request.session['items_total'] = cart.cart_item.count()
        cart.qty = cart.cart_item.count()
        cart.save()
        if cart.total == float(0):
            context = {"empty": True, "empty_message": empty_message}
    else:
        context = {"empty": True, "empty_message": empty_message}
    template = 'cart/cart_home.html'
    return render(request, template, context)


@login_required
def remove_from_cart(request, id):
    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    cart = cartitem.cart
    cart.qty = cart.qty - 1
    cart.save()
    messages.success(request, f'Product successfully removed')
    return HttpResponseRedirect(reverse("cart"))


@login_required
def add_to_cart(request, slug):
    try:
        cart = Cart.objects.filter(user=request.user, active=True).first()
    except:
        pass
    if cart is None:
        print(1)
        cart = Cart(user=request.user)
        cart.save()
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    product_var = [] # product variations
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass
        found = False
        cart_items = CartItem.objects.filter(cart=cart, product=product)
        if cart_items:
            for cart_item in cart_items:
                if list(cart_item.variations.all()) == product_var:
                    found = True
                    cart_item.quantity = cart_item.quantity + int(qty)
                    cart_item.save()
                    cart_item.line_total = float(cart_item.product.price) * float(cart_item.quantity)
                    cart_item.save()
                    break
        if not found:
            print(cart)
            cart_item = CartItem.objects.create(cart=cart, product=product)
            if len(product_var) > 0:
                cart_item.variations.add(*product_var)

            cart_item.quantity = int(qty)
            cart_item.save()
            cart_item.line_total = float(cart_item.product.price) * float(cart_item.quantity)
            cart_item.save()

    return HttpResponseRedirect(reverse("cart"))


@login_required
def decrease_by_one(request, id):
    cart_item = CartItem.objects.get(id=id)
    if cart_item.quantity == 1:
        cart_item.delete()
        cart = cart_item.cart
        cart.qty = cart.qty - 1
        cart.save()
        messages.success(request, f'Product successfully removed')
    else:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.save()
        messages.success(request, f'Product quantity successfully decreased by 1')
    return redirect('cart')


@login_required
def increase_by_one(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.save()
    messages.success(request,f'Product quantity successfully increased by 1')
    return redirect('cart')

