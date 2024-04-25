from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import News


def news_list(request):
    news = News.objects.all().order_by('-published_date')
    # создание HTML-страницы по шаблону news_list.html
    # с заданными параметрами 'news'
    return render(request, 'news_list.html', {'news': news})

