from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MainMenu
from faq.models import Faq
from crm.models import Order
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram
from news.models import News
from games.models import Games


def first_page(request):
    mm_item = MainMenu.objects.all()
    faq_item = Faq.objects.all()
    form = OrderForm()
    news = News.objects.order_by('-date')
    paginator = Paginator(news, 2)
    page_number = request.GET.get('cms/index.html')
    news = paginator.get_page(page_number)
    dict_obj = {
        'mm_item': mm_item,
        'faq_item': faq_item,
        'form': form,
        'news': news,
    }
    return render(request, 'cms/index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'cms/thanks.html', {'name': name})
    else:
        return render(request, 'cms/thanks.html')


def company_page(request):
    mm_item = MainMenu.objects.all()
    dict_obj = {
        'mm_item': mm_item,
    }
    return render(request, 'cms/company.html', dict_obj)


def faq_page(request):
    mm_item = MainMenu.objects.all()
    faq_item = Faq.objects.all()
    dict_obj = {
        'mm_item': mm_item,
        'faq_item': faq_item,
    }
    return render(request, 'cms/faqpage.html', dict_obj)


def contacts_page(request):
    mm_item = MainMenu.objects.all()
    faq_item = Faq.objects.all()
    form = OrderForm()
    dict_obj = {
        'mm_item': mm_item,
        'form': form,
    }
    return render(request, 'cms/contacts.html', dict_obj)


def news_page(request):
    news = News.objects.order_by('-date')
    mm_item = MainMenu.objects.all()
    dict_obj = {
        'mm_item': mm_item,
        'news': news,
    }
    return render(request, 'cms/news.html', dict_obj)


def games_page(request):
    mm_item = MainMenu.objects.all()
    games = Games.objects.all()
    dict_obj = {
        'mm_item': mm_item,
        'games': games
    }
    return render(request, 'cms/games.html', dict_obj)
