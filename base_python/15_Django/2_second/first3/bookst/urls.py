"""first3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from bookst import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^login$',views.login),
    url(r'^set_session$',views.set_session),
    url(r'^get_session$',views.get_session),
    url(r'^clear_session$',views.clear_session),
    url(r'^change_pwd$',views.change_pwd),#修改密码
    url(r'^change_pwd_action',views.change_pwd_action),#修改密码
    url(r'^set_cookie$',views.set_cookie), #设置cookie
    url(r'^get_cookie$',views.get_cookie),#获取cookie
    url(r'^login_ajax$',views.login_ajax),
    url(r'^login_ajax_check$',views.login_ajax_check), #ajax登录校验
    url(r'^ajax_handle$',views.ajax_handle),
    url(r'^test_ajax$',views.ajax_test),
    url(r'^login_check$',views.login_check),
    #url(r'^showarg(\d+)',views.show_arg), #位置参数
    url(r'^showarg(?P<num>\d+)',views.show_arg), #关键字参数
]
