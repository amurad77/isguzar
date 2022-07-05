from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from comments.models import ArticleComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contact.forms import SubscribeForm
from article.models import Article
from django.contrib import messages
from core.models import ArticleTags
from comments.forms import ArticleCommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.





def marketing(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    marketing_articles = Article.objects.filter(tags='1')
    print('----------------------------------------------------------------------------------')
    print(marketing_articles)
    print('----------------------------------------------------------------------------------')
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    page_num = request.GET.get('page', 1)

    paginator = Paginator(marketing_articles, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'marketing_articles' : marketing_articles,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'marketing.html', context)


def brand_stories(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    brand_stories = Article.objects.filter(tags='5')
    print('----------------------------------------------------------------------------------')
    print(brand_stories)
    print('----------------------------------------------------------------------------------')

    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(brand_stories, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'brand_stories' : brand_stories,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'brand_stories.html', context)


def human_resources(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    human_resources = Article.objects.filter(tags='2')
    print('----------------------------------------------------------------------------------')
    print(human_resources)
    print('----------------------------------------------------------------------------------')
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    page_num = request.GET.get('page', 1)

    paginator = Paginator(human_resources, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'human_resources' : human_resources,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'human_resources.html', context)


def logistics(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    logistics = Article.objects.filter(tags='3')
    print('----------------------------------------------------------------------------------')
    print(logistics)
    print('----------------------------------------------------------------------------------')
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    page_num = request.GET.get('page', 1)

    paginator = Paginator(logistics, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'logistics' : logistics,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'logistics.html', context)


def health(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    health = Article.objects.filter(tags='4')
    print('----------------------------------------------------------------------------------')
    print(health)
    print('----------------------------------------------------------------------------------')
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    page_num = request.GET.get('page', 1)

    paginator = Paginator(health, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'health' : health,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'health.html', context)



def article_detail(request, slug):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    article = get_object_or_404(Article, slug = slug)
    CommentForm = ArticleCommentForm(request.POST or None)

    if CommentForm.is_valid():
        comment = CommentForm.save(commit = False)
        comment.article = article
        comment.save()
        return HttpResponseRedirect(article.get_absolute_url())

    article_comments_count_detail = ArticleComments.objects.filter(article=article)


    views = article.views
    views += 1
    degis = Article.objects.filter(slug = slug).update(views = views)

    context = {
        'article_comments_count_detail' : article_comments_count_detail,
        'article' : article,
        'form': form,
        'CommentForm' : CommentForm,
        'last7_brend': last7_brend
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


def article(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
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
        'article': page_obj.object_list,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }
    return render (request, 'article.html', context)


def popular_article(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]

    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
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
        'popular_article': page_obj.object_list,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }
    return render (request, 'popular_article.html', context)


def search(request):
    last7_brend = Article.objects.filter(tags='5')[0:][:7]

    form = SubscribeForm()
    if request.method == 'POST':
        subscribe_data = request.POST
        form = SubscribeForm(data = subscribe_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            return HttpResponseRedirect('/')
            print('Form save')
        else:
            print('Form is invalid')


    context = {
        'last7_brend': last7_brend,
        'form': form
    }

    return render(request, 'search.html', context)
