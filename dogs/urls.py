
from django.urls import path

from dogs.views import index, breed, breed_item, DogCreateView, DogUpdateView

app_name = 'dogs'

urlpatterns = [
    path('', index, name='index'),
    path('breed/', breed, name='breed'),
    path('breed/<int:pk>/', breed_item, name='breed_item'),
    path('breed/<int:breed_id>/create_dog/', DogCreateView.as_view(), name='dog_create'),
    # path('dog/create/', DogCreateView.as_view(), name='dog_create'),
    path('dog/<int:pk>/edit/', DogUpdateView.as_view(), name='dog_update')
]