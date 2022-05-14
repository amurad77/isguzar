from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from news.models import News
from comments.models import NewsComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from article.models import Article
from django.db.models import Q
from comments.forms import NewsCommentForm
from django.contrib.auth.decorators import login_required
# from core.forms import SubscribeForm
# Create your views here.
# Create your views here.



def news_detail(request, slug):
    news = get_object_or_404(News, slug = slug)
    # article = get_object_or_404(Article, slug = slug)
    form = NewsCommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.news = news
        comment.save()
        return HttpResponseRedirect(news.get_absolute_url())
    # a = NewsComments.objects.all()
    news_comments_count_detail = NewsComments.objects.filter(news=news)
    print(news_comments_count_detail)

    views = news.views
    views += 1
    degis = News.objects.filter(slug = slug).update(views = views)


    context = {
        'news_comments_count_detail' : news_comments_count_detail,
        'news' : news,
        'form' : form,
    }
    # print(news.comment.all())
    return render(request, 'detail_news.html', context)



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