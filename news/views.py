from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from news.models import News
from comments.models import NewsComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contact.forms import SubscribeForm
from django.contrib import messages
from article.models import Article
# from article.models import Article
from django.db.models import Q
from comments.forms import NewsCommentForm
from django.contrib.auth.decorators import login_required
# from core.forms import SubscribeForm
# Create your views here.
# Create your views here.


def business(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    business_news = News.objects.filter(tags='2')
    print('----------------------------------------------------------------------------------')
    print(business_news)
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

    paginator = Paginator(business_news, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'business_news' : business_news,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'businnes.html', context)


def sciene_and_technology(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    sciene_and_technology_news = News.objects.filter(tags='1')
    print('----------------------------------------------------------------------------------')
    print(sciene_and_technology_news)
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

    paginator = Paginator(sciene_and_technology_news, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'sciene_and_technology' : sciene_and_technology_news,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'sciene_and_technology.html', context)


def design_and_innovation(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    design_and_innovation_news = News.objects.filter(tags='3')
    print('----------------------------------------------------------------------------------')
    print(design_and_innovation_news)
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

    paginator = Paginator(design_and_innovation_news, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'design_and_innovation' : design_and_innovation_news,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'design_and_innovation.html', context)


def art_and_culture(request):
    last7_brend = Article.objects.filter(tags='5').order_by('-id')[0:7]
    art_and_culture_news = News.objects.filter(tags='4')
    print('----------------------------------------------------------------------------------')
    print(art_and_culture_news)
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

    paginator = Paginator(art_and_culture_news, 5) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'art_and_culture' : art_and_culture_news,
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
    }

    return render(request, 'art_and_culture.html', context)


def news_detail(request, slug):
    # a = get_object_or_404(News, title=slug)
    # the_next = title.get_next_by_created_at()




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


    news = get_object_or_404(News, slug = slug)
    # the_next = news.get_next_by_created_at()
    # article = get_object_or_404(Article, slug = slug)
    CommentForm = NewsCommentForm(request.POST or None)

    if CommentForm.is_valid():
        comment = CommentForm.save(commit = False)
        comment.news = news
        comment.save()
        return HttpResponseRedirect(news.get_absolute_url())
    # a = NewsComments.objects.all()
    news_comments_count_detail = NewsComments.objects.filter(news=news)
    
    print(news_comments_count_detail)

    views = news.views
    views += 1
    degis = News.objects.filter(slug = slug).update(views = views)
    # queryset = get_object_or_404(News, slug=slug)
    
    # the_next = queryset.get_next_by_created_at()
     
    # the_prev= queryset.get_previous_by_created_at()

    

    context = {
        # "the_next" : the_next,
        # "the_prev": the_prev,
        'news_comments_count_detail' : news_comments_count_detail,
        'news' : news,
        'CommentForm' : CommentForm,
        'form': form,
        'last7_brend': last7_brend,
    }

    # print(news.comment.all())
    return render(request, 'detail_news.html', context)




def news(request):

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
        'page_obj': page_obj,
        'form': form,
        'last7_brend': last7_brend
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



