from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.shortcuts import redirect


def logout_views(request):
    logout(request)
    return redirect('home')

class SignUpView(CreateView) :
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


