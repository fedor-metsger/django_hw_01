
from django.urls import path

from catalog.views import contacts, ProductDetailView, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    # path('product/<int:pk>/', product, name='product')
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]