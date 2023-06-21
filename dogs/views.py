
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.forms import inlineformset_factory

from dogs.models import Breed, Dog, Ancestor
from dogs.forms import DogForm, AncestorForm


# Create your views here.
def index(request):
    context = {"breeds": Breed.objects.all()[:3]}

    # return render(request, "dogs/base.html", context=context)
    return render(request, "dogs/index.html", context=context)

def breed(request):
    context = {"breeds": Breed.objects.all()}

    return render(request, "dogs/breeds.html", context=context)

def breed_item(request, pk):
    breed = Breed.objects.filter(pk=pk)[0].name
    context = {
        "breed": breed,
        "breed_id": pk,
        "owner_id": request.user.id,
        "dogs": Dog.objects.filter(breed_id=pk)
    }
    return render(request, "dogs/breed_item.html", context=context)

class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        breed_id = self.kwargs["breed_id"]
        kwargs.update({'breed_id': breed_id})
        owner_id = self.request.user.id
        kwargs.update({'owner_id': owner_id})
        return kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dogs:breed_item', kwargs={'pk': self.kwargs["breed_id"]})

class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.breed_id = Dog.objects.get(pk=self.kwargs["pk"]).breed.id
        kwargs.update({'breed_id': self.breed_id})
        # owner_id = self.request.user.id
        owner_id = None
        kwargs.update({'owner_id': owner_id})
        return kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dogs:breed_item', kwargs={'pk': self.breed_id})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        AncestorFormSet = inlineformset_factory(Dog, Ancestor, form=AncestorForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = AncestorFormSet(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = AncestorFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)