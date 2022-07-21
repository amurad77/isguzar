from django.contrib import admin
from .models import News

# # Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'descrtiption', 'created_at', 'updated_at')
    list_filter = ('descrtiption', 'created_at', 'updated_at')
    search_fields = ('descrtiption', 'created_at', 'updated_at')

admin.site.register (News, NewsAdmin)

