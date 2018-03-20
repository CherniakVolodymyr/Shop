from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


# Create your views here.
def ind(request):
    name = 'Volodymyr'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form)
        print(form.cleaned_data)

        new_form = form.save()
    return render(request, 'shop/index.html', locals())


def home(request):
    product = ProductImage.objects.filter(is_active=True)
    # products_images_phones = products_images.filter(product__category__id=1)
    # products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'shop/home.html', locals())
