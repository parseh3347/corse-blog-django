from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import PostNewModel
from .forms import PostForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class PostNewView(CreateView):
    model = PostNewModel
    template_name = 'registration/postnew.html'
    form_class = PostForm
    # success_url = reverse_lazy('home')