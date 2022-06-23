"""isguzar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    career_center,
    career_center_detail,
    searchbar,
    
)

from contact.views import (
    contact,
    author
)

from news.views import (
    news,
    news_detail
)
from article.views import (
    article,
    article_detail,
    search,
    popular_article
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact, name = 'contact'),
    path('career_center/', career_center, name = 'career_center'),
    path('news_detail/<slug:slug>/', news_detail, name = 'detail_news'),
    path('news/', news),
    path('author/', author)
    path('article/', article),
    path('popular_article/', popular_article),
    path('article_detail/<slug:slug>/', article_detail, name = 'article_detail'),
    path('career_center_detail/<slug:slug>/', career_center_detail, name = 'career_center_detail'),
    path('search/', search),
    path('searchbar/', searchbar, name = 'searchbar'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)