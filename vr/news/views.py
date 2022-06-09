from django.shortcuts import render, get_object_or_404
from .models import News
from cms.models import MainMenu


def news(request):
    news = News.objects.order_by('-date')
    mm_item = MainMenu.objects.all()
    dict_obj = {
        'mm_item': mm_item,
        'news': news,
    }
    return render(request, 'cms/news.html', dict_obj)


def detail(request, post_id):
    mm_item = MainMenu.objects.all()
    post = get_object_or_404(News, pk=post_id)
    dict_obj = {
        'mm_item': mm_item,
        'post': post,
    }
    return render(request, "cms/details.html", dict_obj)
