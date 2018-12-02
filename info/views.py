from django.shortcuts import render
from info.models import News


# Create your views here.
def info_view(request):
    news = News.objects.all();
    return render(request, 'info/index.html', context={'news': news})


def news_detail(request, slug):
    news_item = News.objects.get(slug__iexact=slug)
    return render(request, 'info/news_detail.html', context={'news_item': news_item})

