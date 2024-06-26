from django.urls import path

from . import views

app_name = 'registration'

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]
