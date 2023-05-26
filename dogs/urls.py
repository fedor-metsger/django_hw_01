
from django.urls import path

from dogs.views import index, breed, breed_item

app_name = 'dogs'

urlpatterns = [
    path('', index, name='index'),
    path('breed/', breed, name='breed'),
    path('breed/<int:pk>/', breed_item, name='breed_item')
]