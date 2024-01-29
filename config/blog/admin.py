from django.contrib import admin

from .models import Post, Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'author', 'excerpt', 'date', 'photo' ]
    search_fields = ['titel', 'author']
    list_display_links = ['title', 'author']
    date_hierarchy = 'date'
    list_filter = ['author', 'date', 'title' ]
    raw_id_fields = ['author']

# admin.site.register(Comment)
@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''

    list_display = ('author','post' ,'body' ,'date' )
    list_filter = ('author',)
    raw_id_fields = ('author',)
    # readonly_fields = ('',)
    search_fields = ('author','post')
    date_hierarchy = 'date'
    ordering = ('author',)