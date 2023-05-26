from django.contrib import admin

from dogs.models import Breed, Dog

# Register your models here.
@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description",)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "breed", "birthdate",)
    list_filter = ("breed",)
    search_fields = ("name", "breed",)