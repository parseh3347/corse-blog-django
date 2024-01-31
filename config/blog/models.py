from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    date = models.DateField(default = date.today)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d',default='null')
    
    def __str__(self):
        return self.title
    
    #برای هر شی از پست بالا یک یوآرال درنظر بگیر
    # وقتی ما پست را آپدیت می کنیم بتونه به هرکدام از شی های بالا  زیدایرکت کنه
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser',on_delete = models.CASCADE,related_name='comments')
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) :
        return self.body

