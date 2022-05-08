from django.shortcuts import render, get_object_or_404
from core.models import Articles
# Create your views here.

def home(request):
    article = Articles.objects.all().order_by('-id')[:1]
    article2 = Articles.objects.all().order_by('-id')[1:] [:1]
    article3 = Articles.objects.all().order_by('-id') [2:] [:1]


    context = {
        'article' : article,
        'article2' : article2,
        'article3' : article3

    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(Articles, slug = slug)

    context = {
        'news' : news,
    }

    return render(request, 'detailnews.html', context)



def news(request):
    news = Articles.objects.all().order_by('-id')

    context = {
        'news': news
    }
    return render (request, 'news.html', context)