from django.conf.urls import url
from . import views
# 如果在url中写成 url('login/',views.login,name='login'),会导致login和do_login混淆，访问do_login会访问到login界面
# 原因未知
urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^do_login/',views.do_login,name='do_login'),
    url(r'^test/',views.test,name='test'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^t_mine',views.t_mine,name='t_mine'),
    url(r'^t_login',views.t_login,name='t_login'),
]