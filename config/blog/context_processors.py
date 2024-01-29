from .models import Post


def resent_posts(request):
    resent_posts = Post.objects.order_by('-date')[:5]
    return {'resent_posts': resent_posts}