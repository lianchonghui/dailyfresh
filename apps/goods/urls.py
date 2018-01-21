from django.conf.urls import url, patterns, include
from . import views


'''
路由配置
patterns参数是多个url()函数返回的对象
#第一个参数(字符串)指定视图所在的位置,如果有指定,则第二个之后的views写法可以简写
# (?P<id>pattern)匹配和获取,如:(?P<page>\d+),匹配到一个或多个数字,并将值赋给page
# 如果没有?P<id>,只有(pattern)则按顺序赋值给views中的方法中的参数

注意:
django的路由前面是不需要加/
'''

urlpatterns = patterns(
    '',
    url(r'^$', views.home_list_page),
    url(r'^detail/(\d+)$', views.goods_detail),
    url(r'^list/(?P<goods_type_id>\d+)/(?P<page>\d+)$', views.goods_list),
    url(r'^search$', views.MySearchView.as_view()),
    # url(r'^search/', include('haystack.urls')),
)
