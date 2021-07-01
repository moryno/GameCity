from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    visits = request.session.get('visits', 1)
    request.session['visits'] = visits + 1
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'catalog/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'visits': visits, })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'catalog/product/detail.html',
                  {'product': product})



