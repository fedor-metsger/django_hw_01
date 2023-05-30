
from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.utils.text import slugify

from blog.models import Article

class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Блог'
    }
    def get_queryset(self):
        queryset = super().get_queryset().filter(published=True).order_by('id')
        return queryset

class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(request, *args, **kwargs):
        context = super().get_context_data()
        Article.objects.filter(pk=context["object"].pk).update(views=context["object"].views + 1)
        context["object"].views += 1
        return context


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'slug', 'content',)  # Поля для заполнения при создании
    success_url = reverse_lazy('articles:list')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        # slug = request.POST.get('slug')
        slug = slugify(title)
        content = request.POST.get('content')
        # print(f'Получена информация: {title}, slug: {slug}, содержимое: {content}')
        if title and title != "":
            Article.objects.create(title=title, slug=slug, content=content,
                                   creation_date=datetime.now(), published=True, views=0)
        return redirect('/article/')

class ArticleDeleteView(DeleteView):
    model = Article # Модель
    success_url = reverse_lazy('articles:list') # Адрес для перенаправления после успешного удаления

class ArticleUpdateView(UpdateView):
    model = Article # Модель
    fields = ('title', 'slug', 'content',)
    success_url = reverse_lazy('articles:article')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        published = request.POST.get('published')
        checked = (published == "on")
        content = request.POST.get('content')
        # print(f'Получена информация: {title}, slug: {slug}, содержимое: {content}')
        if title and slug:
            Article.objects.filter(pk=kwargs["pk"]).update(title=title,
                                                           slug=slug, content=content,
                                                           published=checked)
        return redirect(f'/article/{Article.objects.filter(pk=kwargs["pk"])[0].id}/')