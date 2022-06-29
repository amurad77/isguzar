from django.urls import path, include
# from django.conf.urls import url
from .views import news


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
]