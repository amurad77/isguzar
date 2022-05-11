from django.contrib import admin
from .models import ArticleComments, NewsComments
# Register your models here.


class ArticleCommentAdmin(admin.ModelAdmin):
    class Meta:
        model = ArticleComments

    list_display = ('name', 'mail', 'created_at', 'approved_comment')
    # list_filter = ('name', 'created_at', 'approved_comment')
    search_fields = ('name', 'created_at', 'approved_comment')

admin.site.register (ArticleComments, ArticleCommentAdmin)



class NewsCommentAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsComments

    list_display = ('name', 'mail', 'created_at', 'approved_comment')
    # list_filter = ('name', 'created_at', 'approved_comment')
    search_fields = ('name', 'created_at', 'approved_comment')

admin.site.register (NewsComments, NewsCommentAdmin)

