from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_at')

    search_fields = ('title', 'author', 'content')

    list_filter = ('created_at',)

    ordering = ( 'author' ,'-created_at',)

admin.site.register(Category)
admin.site.register(Tag)