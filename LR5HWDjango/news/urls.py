from django.urls import path, re_path

from . import views

app_name = 'news'
urlpatterns = [
    path(r'', views.news_list, name='news_list')
]