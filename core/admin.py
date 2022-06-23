from django.contrib import admin
from .models import CareerCenter, DesiredFeautures, Tags
# Register your models here.



class DesiredFeauturesInline(admin.TabularInline):
    model = DesiredFeautures

class CareerCenterAdmin(admin.ModelAdmin):
    inlines = [DesiredFeauturesInline]
    list_display = ('title', 'mail', 'created_at', 'updated_at')
    list_filter = ('mail', 'created_at', 'updated_at')
    search_fields = ('mail', 'created_at', 'updated_at')

admin.site.register(CareerCenter, CareerCenterAdmin)


admin.site.register(Tags)