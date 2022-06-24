from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from news.models import News
from comments.models import NewsComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CareerCenter, DesiredFeautures
from article.models import Article
from django.db.models import Q
from comments.forms import NewsCommentForm
from contact.forms import SubscribeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from core.forms import SubscribeForm
# Create your views here.

def home(request):
    form = SubscribeForm()
    submitted = False

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






    career_center_home = CareerCenter.objects.all().order_by('-id')[:9]
    





    query = request.GET.get('q')
    querylist = News.objects.all()
    # news = News.objects.all()
    news1 = News.objects.all().order_by('-id')[:1]
    news2 = News.objects.all().order_by('-id')[1:] [:1]
    news3 = News.objects.all().order_by('-id') [2:] [:1]
    article = Article.objects.all().order_by('-id')[0:] [:5]
    popular_list1 = Article.objects.all().order_by('-views', '-id')[:1]
    popular_list2 = Article.objects.all().order_by('-views', '-id')[1:] [:1]
    popular_list3 = Article.objects.all().order_by('-views', '-id')[2:] [:1]
    news_comments_count = NewsComments.objects.filter()
    print(news1)
    # news_comments = News.objects.comments.all()

    context = {
        'news1' : news1,
        'news2' : news2,
        'news3' : news3,
        'article' : article,
        'popular_list1' : popular_list1,
        'popular_list2' : popular_list2,
        'popular_list3' : popular_list3,
        'form' : form,
        'news_comments_count' : news_comments_count,
        'career_center_home' : career_center_home,


    }
    return render(request, 'index.html', context)

def career_center(request):
    career_center = CareerCenter.objects.all().order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(career_center, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'career_center': page_obj.object_list,
        'page_obj': page_obj
    }

    return render(request, 'career_center.html', context)



def career_center_detail(request, slug):
    career_center_related = CareerCenter.objects.all().order_by('-id')[:3]

    career_center = get_object_or_404(CareerCenter, slug = slug)
    desired_features = DesiredFeautures.objects.filter(career_center = career_center)
    print(career_center)
    print(desired_features)
    views = career_center.views
    views += 1
    degis = CareerCenter.objects.filter(slug = slug).update(views = views)

    context = {
        'career_center_related' : career_center_related,
        'desired_features' : desired_features,
        'career_center' : career_center,
    }
    return render(request, 'career_center_detail.html', context)



def searchbar(request):



    if request.method == 'GET':
        search = request.GET.get('search')
        post = News.objects.all().filter(title__icontains=search)

        return render(request, 'search.html', {'post' : post})

    







