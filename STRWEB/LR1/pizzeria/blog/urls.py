# blog/urls.py
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_company, name='about_company'),
    path('news/', views.news_list, name='news_list'),
    path('faq/', views.faq_list, name='faq_list'),
    path('promo/', views.promo_list, name='promo_list'),
    path('reviews/', views.review_list, name='reviews'),
]
