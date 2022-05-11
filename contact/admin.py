from django.contrib import admin
from .models import Subscribe, Contact
# Register your models here.

# class ContactAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Contact

#     list_display = ('name', 'email', 'created_at', 'updated_at')
#     list_filter = ('name', 'created_at', 'updated_at')
#     search_fields = ('name', 'created_at', 'updated_at')

admin.site.register (Contact)

admin.site.register(Subscribe)
