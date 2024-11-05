from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    filter = request.GET.get('sort')
    phone_objects = Phone.objects.all()

    if filter == 'name':
        phone_objects = Phone.objects.all().order_by('name')

    elif filter == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')

    elif filter == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')

    context = {
        'phones': phone_objects
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.get(slug=slug)
    phone = {
        'name': p.name,
        'id': p.id,
        'image': p.image,
        'price': p.price,
        'release_date': p.release_date,
        'lte_exist': p.lte_exists

    }

    context = {
        'phone': phone
    }
    return render(request, template, context)
