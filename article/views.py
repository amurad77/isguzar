from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from comments.models import ArticleComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article
from comments.forms import ArticleCommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def article_detail(request, slug):
    article = get_object_or_404(Article, slug = slug)
    form = ArticleCommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.article = article
        comment.save()
        return HttpResponseRedirect(article.get_absolute_url())


    views = article.views
    views += 1
    degis = Article.objects.filter(slug = slug).update(views = views)

    context = {
        'article' : article,
        'form' : form,
    }
    # print(news.comment.all())
    return render(request, 'detail_article.html', context)

def add_comment_to_post(request, pk):
    article = Article.get_object_or_404(Article, pk = pk)

    if request.POST == 'POST':
        form = ArticleComments(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk = article.pk)
    else:
        form = ArticleCommentForm()
    return render(request, 'forms.html', {'form' : form})








# def home(request):
#     home = Article.objects.all().order_by('-id') [2:] [:1]
#     popular_list = Article.objects.all().order_by('-views', '-id')[:1]


#     context = {
#         'article' : article,

#     }
#     return render(request, 'index.html', context)

def article(request):
    article = Article.objects.all().order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(article, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'article': page_obj.object_list,
        'page_obj': page_obj
    }
    return render (request, 'article.html', context)



def popular_article(request):
    popular_article = Article.objects.all().order_by('-views')


    page_num = request.GET.get('page', 1)

    paginator = Paginator(popular_article, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'popular_article': page_obj.object_list,
        'page_obj': page_obj
    }
    return render (request, 'popular_article.html', context)


def search(request):
    return render(request, 'search.html')