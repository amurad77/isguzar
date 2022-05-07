from django.shortcuts import render
from core.models import Articles
# Create your views here.

def home(request):
    article = Articles.objects.all().order_by('-id')[:4]
    article2 = Articles.objects.all().order_by('id')[3:4]

    context = {
        'article' : article,
        'article2' : article2,
    }
    return render(request, 'index.html', context)