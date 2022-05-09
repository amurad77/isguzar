from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from core.models import News
from comments.models import NewsComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article
from django.db.models import Q
from comments.forms import NewsCommentForm, SubscribeForm
from django.contrib.auth.decorators import login_required
# from core.forms import SubscribeForm
# Create your views here.

def home(request):

    form = SubscribeForm()

    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            print('Form save')
        else:
            print('Form is invalid')


    query = request.GET.get('q')
    querylist = News.objects.all()

    news = News.objects.all().order_by('-id')[:1]
    news2 = News.objects.all().order_by('-id')[1:] [:1]
    news3 = News.objects.all().order_by('-id') [2:] [:1]
    article = Article.objects.all().order_by('-id')[0:] [:5]
    popular_list1 = Article.objects.all().order_by('-views', '-id')[:1]
    popular_list2 = Article.objects.all().order_by('-views', '-id')[1:] [:1]
    popular_list3 = Article.objects.all().order_by('-views', '-id')[2:] [:1]


    context = {
        'news' : news,
        'news2' : news2,
        'news3' : news3,
        'article' : article,
        'popular_list1' : popular_list1,
        'popular_list2' : popular_list2,
        'popular_list3' : popular_list3,
        'form' : form,

    }
    return render(request, 'index.html', context)





def news_detail(request, slug):
    news = get_object_or_404(News, slug = slug)
    article = get_object_or_404(Article, slug = slug)
    form = NewsCommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.news = news
        comment.save()
        return HttpResponseRedirect(news.get_absolute_url())


    views = news.views
    views += 1
    degis = News.objects.filter(slug = slug).update(views = views)

    context = {
        'news' : news,
        'form' : form,
    }
    # print(news.comment.all())
    return render(request, 'detail_news.html', context)

def add_comment_to_post(request, pk):
    news = News.get_object_or_404(News, pk = pk)

    if request.POST == 'POST':
        form = NewsCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.news = news
            comment.save()
            return redirect('detail_news', pk = news.pk)
    else:
        form = NewsCommentForm()
    return render(request, 'forms.html', {'form' : form})



@login_required
def comment_is_published(request, pk):
    comment = get_object_or_404(Comments, pk = pk)
    comment.is_published()
    return redirect('detail_news', pk = comment.news.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    return redirect('detail_news', pk = comment.news.pk)


def news(request):
    news = News.objects.all().order_by('-id')

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


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = News.objects.all().filter(title__icontains=search)
        return render(request, 'search.html', {'post' : post})