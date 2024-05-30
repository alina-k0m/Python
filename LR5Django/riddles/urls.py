from django.urls import path, re_path

from . import views

app_name = 'riddles'

urlpatterns = [
    path(r'', views.index, name='index'),
    re_path('^([0-9]+)/$', views.detail, name='detail'),
    re_path('^([0-9]+)/answer/$', views.answer, name='answer'),
    re_path('^register/$', views.RegisterFormView.as_view()),
    re_path('^login/$', views.LoginFormView.as_view()),
    re_path('^logout/$', views.LogoutView.as_view()),
    re_path('^password-change/', views.PasswordChangeView.as_view()),
    # отправка сообщения
    re_path('^([0-9]+)/post/$', views.post, name='post'),
    # отправка списка сообщений
    re_path('^([0-9]+)/msg_list/$', views.msg_list, name='msg_list')


]


