from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

class PostNewView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'registration/postnew.html'
    success_url = reverse_lazy('home')