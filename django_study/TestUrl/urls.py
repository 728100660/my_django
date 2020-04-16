from django.conf.urls import url
from . import views
urlpatterns = [
    url('test/',views.test,name='test'),
    url('test2/',views.test2,name='test2'),
    url('test3/',views.test3,name='test3'),
    url('test4/',views.test4,name='test4'),
    url('home/',views.home,name='home'),
    url('Post/',views.Post,name='Post'), 
    url('Get/(\d+)/',views.Get,name='Get'),
]