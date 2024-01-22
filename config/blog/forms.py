
from django import forms
from .models import PostNewModel


class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostNewModel
        fields = ["title","excerpt","body","author","date","photo"]
