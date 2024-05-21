from django.urls import path

from . import views

app_name = 'pizza'

urlpatterns = [path('', views.homepage, name='homepage')]
