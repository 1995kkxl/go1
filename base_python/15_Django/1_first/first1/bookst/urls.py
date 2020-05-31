from django.conf.urls import url
from bookst import views

urlpatterns = [
    url(r'^index$', views.index),
    # re_path('^index2', views.index2, name='index2'),
    url(r'^index2$', views.index2),  # 指定视图函数
    url(r'^books$', views.show_books),  # 指定视图函数
    url(r'^books/(\d+)$', views.detail),  # 指定视图函数
    # 意思是,当浏览器输入127.0.0.1:port/index/的时候,让views.py中index函数来处理
]