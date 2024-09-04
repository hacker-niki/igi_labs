# Create your views here.
from django.shortcuts import render
from pizza.models import PromoCode

from .models import Post, CompanyInfo, FAQ


def home(request):
    latest_post = Post.objects.order_by('-published_date').first()
    return render(request, 'blog/home.html', {'latest_post': latest_post})


def about_company(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'blog/about_company.html', {'company_info': company_info})


def news_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/news_list.html', {'posts': posts})


def faq_list(request):
    faqs = FAQ.objects.all().order_by('-added_date')
    return render(request, 'blog/faq_list.html', {'faqs': faqs})


def promo_list(request):
    promos = PromoCode.objects.all().order_by('-is_active')
    for promo in promos:
        promo.discount *= 100
    return render(request, 'blog/promo_list.html', {'promos': promos})
