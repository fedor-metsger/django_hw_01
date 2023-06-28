
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from catalog.models import Contact, Product, Version
from catalog.forms import ProductForm, VersionForm


class ProductListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    redirect_field_name = "redirect_to"

    model = Product
    extra_context = {
        'title': 'Главная страница'
    }
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-creation_date')[:6]
        return queryset

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["moderator"] = "moderator" in [i.name for i in self.request.user.groups.all()]
        return context_data

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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        owner_id = self.request.user.id
        kwargs.update({'owner_id': owner_id})
        return kwargs

class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_authenticated and (
                obj.owner_id == self.request.user.id or
                "moderator" in [i.name for i in self.request.user.groups.all()])

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:product', kwargs = {'pk': self.object.id})

    def get_formset(self):
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == "POST":
            return VersionFormSet(self.request.POST, instance=self.object)
        else:
            return VersionFormSet(instance=self.object)

    def form_invalid(self, form):
        self.formset = self.get_formset()
        self.formset.is_valid()
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = getattr(self, 'formset', self.get_formset())
        obj = self.get_object()
        context_data["owner"] = obj.owner_id == self.request.user.id
        return context_data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["moderator"] = "moderator" in [i.name for i in self.request.user.groups.all()]
        obj = self.get_object()
        kwargs["owner"] = obj.owner_id == self.request.user.id
        return kwargs

    def form_valid(self, form):
        formset = self.get_formset()

        curr = False
        for f in formset.forms:
            if "cleaned_data" in f and "current" in f.cleaned_data:
                if f.cleaned_data["current"]:
                    if not curr: curr = True
                    else:
                        form.add_error(None, ValidationError("Может быть только одна активная версия продукта!"))
                        return super().form_invalid(form)
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:index")