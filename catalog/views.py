
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.forms import inlineformset_factory

from catalog.models import Contact, Product, Version
from catalog.forms import ProductForm, VersionForm

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница'
    }
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-creation_date')[:6]
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

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:product', kwargs = {'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:index")