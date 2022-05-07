from django.contrib import admin
from .models import Articles, Comment, Subscribe
# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'descrtiption', 'created_at', 'updated_at')
    list_filter = ('descrtiption', 'created_at', 'updated_at')
    search_fields = ('descrtiption', 'created_at', 'updated_at')

admin.site.register (Articles, ArticlesAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'created_at', 'updated_at')
    list_filter = ('subject', 'created_at', 'updated_at')
    search_fields = ('subject', 'created_at', 'updated_at')

admin.site.register (Comment, CommentAdmin)

admin.site.register(Subscribe)