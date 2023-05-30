
from django.urls import path

from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView
from blog.views import ArticleDeleteView, ArticleUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
    path('create/', ArticleCreateView.as_view(), name='create')
]