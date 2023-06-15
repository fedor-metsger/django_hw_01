
from django.urls import path

from catalog.views import contacts, ProductDetailView, ProductListView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create')
]