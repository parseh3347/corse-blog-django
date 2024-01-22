from django.db import models
from django.views.generic import CreateView
from datetime import date
# Create your models here.

class PostNewModel(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    date = models.DateField(default = date.today)
    photo = models.ImageField(upload_to='photo/%y/%m/%d')
    
    
    def __str__(self):
        return self.title