from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'winRate'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
