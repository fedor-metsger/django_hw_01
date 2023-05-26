from django.http import HttpResponse
from django.shortcuts import render

from dogs.models import Breed, Dog


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
        "dogs": Dog.objects.filter(breed_id=pk)
    }

    return render(request, "dogs/breed_item.html", context=context)

