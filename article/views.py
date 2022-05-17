from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from comments.models import ArticleComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contact.forms import SubscribeForm
from article.models import Article
from django.contrib import messages

from comments.forms import ArticleCommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def article_detail(request, slug):


    formSubscribe = SubscribeForm()
    submitted = False

    if request.method == 'POST':
        subscribe_data = request.POST
        formSubscribe = SubscribeForm(data = subscribe_data)
        if formSubscribe.is_valid():
            formSubscribe.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/article_detail?submitted=True')
            print('Form save')
        else:
            print('Form is invalid')


    article = get_object_or_404(Article, slug = slug)
    form = ArticleCommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.article = article
        comment.save()
        return HttpResponseRedirect(article.get_absolute_url())

    article_comments_count_detail = ArticleComments.objects.filter(article=article)


    views = article.views
    views += 1
    degis = Article.objects.filter(slug = slug).update(views = views)

    context = {
        'formSubscribe': formSubscribe,
        'article_comments_count_detail' : article_comments_count_detail,
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

    form = SubscribeForm()
    submitted = False

    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/article?submitted=True')
            print('Form save')
        else:
            print('Form is invalid')




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
        'form': form,
        'article': page_obj.object_list,
        'page_obj': page_obj
    }
    return render (request, 'article.html', context)



def popular_article(request):

    form = SubscribeForm()
    submitted = False

    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/popular_article?submitted=True')
            print('Form save')
        else:
            print('Form is invalid')




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
        'form': form,
        'popular_article': page_obj.object_list,
        'page_obj': page_obj
    }
    return render (request, 'popular_article.html', context)


def search(request):
    form = SubscribeForm()
    submitted = False


    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/?submitted=True')
            print('Form save')
        else:
            print('Form is invalid')


    context = {
        'form': form
        }
    return render(request, 'search.html', context)
