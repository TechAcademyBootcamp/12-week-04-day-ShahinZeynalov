from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import News
from django.urls import reverse_lazy

# Create your views here.


class PublishList(ListView):
    model = News
    template_name = 'list.html'
    context_object_name = 'news_list'


class DetailList(DetailView):
    model = News
    template_name='detail_news.html'


class CreateNews(CreateView):
    model = News
    fields='__all__'
    template_name = 'create_news.html'
    success_url= reverse_lazy('home')

class DeleteNews(DeleteView):
    model = News
    template_name = 'delete_news.html'
    success_url= reverse_lazy('home')

class UpdateNews(UpdateView):
    model = News
    fields='__all__'
    success_url= reverse_lazy('home')
    template_name_suffix = '_update_form'
