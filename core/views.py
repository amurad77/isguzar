from django.shortcuts import render, get_object_or_404
from core.models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    page_num = request.GET.get('page', 1)

    paginator = Paginator(news, 5) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'news': page_obj.object_list,
        'page_obj': page_obj
    }
    return render (request, 'news.html', context)