
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.forms import inlineformset_factory

from catalog.models import Contact, Product
from catalog.forms import ProductForm

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница'
    }
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-creation_date')[:5]
        return queryset

class ProductDetailView(DetailView):
    model = Product

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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')