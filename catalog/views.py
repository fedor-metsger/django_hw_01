
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Contact, Product


# Create your views here.
def index(request):
    context = {"products": []}
    for p in Product.objects.order_by('-creation_date')[:5]:
        context["products"].append({"name": p.name, "category": p.category,
                                    "price": p.price, "date": p.creation_date})
    return render(request, "index.html", context=context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(f'Получена контактная информация: {name}, тел.: {phone}, e-mail: {email}')
        if name and (phone or email):
            Contact.objects.create(name=name, phone=phone, email=email)

    context = {"contacts": []}
    for c in Contact.objects.all():
        context["contacts"].append({"name": c.name, "phone": c.phone, "email": c.email})

    return render(request, "contacts.html", context=context)