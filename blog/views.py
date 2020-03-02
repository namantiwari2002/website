from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from cart.models import Cart
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory


def search(request):
    categories = Category.objects.all()
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(name__icontains=q)
        context = {'query': q,
                   'products': products,
                   'categories': categories,
                   }
    else:
        context = {}
    return render(request, 'blog/result.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if request.user.is_authenticated:
        try:
            request.session['items_total'] = Cart.objects.filter(user=request.user, active=True).first().cart_item.count()
        except:
            request.session['items_total'] = 0
        if request.user.profile.club == "None" or request.user.profile.department == 'None':
            messages.warning(request, f'Please update your profile for better experience.')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'blog/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'blog/details.html', context)

@login_required
def manage_products(request):
    if request.method == 'POST':
        ProductFormSet = modelformset_factory(Product, form=ProductForm, extra=0, fields={'name', 'price', 'stock', 'available'})
        data_1 = request.POST.copy()
        total_forms = 0
        for form in ProductFormSet(queryset=Product.objects.filter(merchant=request.user)):
            total_forms = total_forms + 1
        data = {
            'form-TOTAL_FORMS': total_forms,
            'form-INITIAL_FORMS': total_forms,
            'form-MAX_NUM_FORMS': '',
        }
        data_1.update(data)
        formset = ProductFormSet(data_1)
        print(formset.non_form_errors())
        if formset.is_valid:
            formset.save()
            messages.success(request, f'Your Product has been Updated!')
            return redirect('blog:manageproducts')
    error = 0
    ProductFormSet = modelformset_factory(Product, form=ProductForm, extra=0, fields={'name', 'price', 'stock', 'available'})
    formset = ProductFormSet(queryset=Product.objects.filter(merchant=request.user))
    products = Product.objects.filter(merchant=request.user)
    if request.user.profile.is_merchant == 0:
        error = 1
    context = {
        'formset': formset,
        'products': products,
        'error': error,
    }
    template = 'blog/manageproducts.html'
    return render(request, template, context)