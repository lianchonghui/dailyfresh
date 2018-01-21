# coding:utf-8
'''
goods模块
处理上分了三层
    java        - python
    views       - views.py
    service     - logics.py
    dao&pojo    - models.py

在models.py封装了底层操作数据的方法
在logics.py封装了业务上的方法
在views.py上通过logics.py处理数据
'''
from django.views.decorators.http import require_POST
from .logics import GoodsLogic
from utils.views import json_view
from django.shortcuts import render
from .enums import *
from apps.cart.models import Cart
from apps.profile.models import BrowseHistory
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage
from haystack.generic_views import SearchView

'''
1.对常量参数进行枚举处理
2.views调用logics层的方法
3.


扩展:
1.django用户模块的使用
    a.自定义用户验证模块:http://blog.csdn.net/yangyihongyangjiying/article/details/45623865
    b.django的user模块的使用:http://blog.csdn.net/xcy2011sky/article/details/26464993

2.request对象的常用属性:https://www.cnblogs.com/scolia/archive/2016/07/01/5633351.html

3.django的Django Aggregation聚合:https://www.cnblogs.com/linxiyue/p/3906179.html?utm_source=tuicool&utm_medium=referral
'''
def home_list_page(request):
    fruits = GoodsLogic.get_goods_by_type(FRUITS, HOME_ITEM_NUMS) 
    seafood = GoodsLogic.get_goods_by_type(SEAFOOD, HOME_ITEM_NUMS) 
    meat = GoodsLogic.get_goods_by_type(MEAT, HOME_ITEM_NUMS) 
    eggs = GoodsLogic.get_goods_by_type(EGGS, HOME_ITEM_NUMS) 
    vegetables = GoodsLogic.get_goods_by_type(VEGETABLES, HOME_ITEM_NUMS) 
    frozen = GoodsLogic.get_goods_by_type(FROZEN, HOME_ITEM_NUMS) 
    cart = {'goods_num__sum':0}
    '''
    使用request的user对象的is_authenticated()对用户登录进行判断,返回bool值
    '''
    if request.user.is_authenticated():
        '''
        aggregate(Sum()) django的聚合方法,Sum 统计所有条目,更多聚合计算相关见扩展3
        '''
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0
    '''
    render()方法接收三个参数
        request
        模板名称字符串 - django会从settings.py文件中寻找TEMPLATE_DIRS的配置
        字典 - 用户前端渲染,如果键值对名称相等可以用locals()函数,该函数会将所有变量传过去
    render(request, template_name, context=None, content_type=None, status=None, using=None)
    Returns a HttpResponse whose content is filled with the result of calling django.template.
    loader.render_to_string() with the passed arguments.

    render_to_response()方法
    render_to_response(template_name, context=None, context_instance=<object object>, content_type=None, status=None, dirs=<object object>, dictionary=<object object>, using=None)
    Returns a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.

    用法1:只使用settings.py中的processors:TEMPLATE_CONTEXT_PROCESSORS
    return render_to_response('my_template.html', my_data_dictionary, context_instance=RequestContext(request))  

    用法2:自己指定processors
    return render_to_response('template1.html',  
        {'message':'I am the view.'},  
        context_instance=RequestContext(request,processors=[custom_proc]))  

    def custom_proc(request):
        "A context processor that provides 'app', 'user' and 'ip_address'."
        return {
            'app': 'My app',
            'user': request.user,
            'ip_address': request.META['REMOTE_ADDR']
             }
    '''
    return render(request,'index.html', {'fruits':fruits, 'seafood':seafood, 'meat':meat, 'eggs':eggs, 'vegetables':vegetables, 'frozen':frozen, 'cart':cart['goods_num__sum']})


def goods_detail(request, goods_id):
    goods = GoodsLogic.get_one_goods(goods_id)
    comments = goods.sordergoods_set.all().order_by('-create_time')[:30]
    for comment in comments:
        '''
        strftime(format) 格式化时间
        '''
        comment.ctime = comment.create_time.strftime('%Y-%m-%d %H:%M:%S')
        comment.user = comment.sorder.user.username
    new_goods_li = GoodsLogic.get_goods_by_type(goods.goods_type_id, limit=2, sort='new')
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0
        '''
        add_one_object()是自定义的类方法,在utils.BaseModel.add_one_object()中
        '''
        BrowseHistory.add_one_object(user=request.user, goods=goods)
    return render(request, 'detail.html', {'goods':goods, 'cart':cart['goods_num__sum'], 'new_goods_li':new_goods_li, 'comments':comments})


def goods_list(request, goods_type_id, page):
    goods_type_id = int(goods_type_id)
    page = int(page)
    sort = request.GET.get('sort', 'default')
    new_goods_li = GoodsLogic.get_goods_by_type(goods_type_id, limit=2, sort='new')
    goods_li_all = GoodsLogic.get_goods_by_type(goods_type_id, sort=sort)
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0

    '''Paginator - django分页功能
    https://www.cnblogs.com/kongzhagen/p/6640975.html
    https://www.168seo.cn/jianzhan/django/2945.html
    '''
    '''
    Paginator(QuerySet,n) - n条数为一页
    '''
    paginator = Paginator(goods_li_all, LIST_PAGE_CAPACITY)
    '''
    painator.page(page)取QuerySet的第page分页对象
    '''
    try:
        goods_li = paginator.page(page)
    except EmptyPage:
        goods_li = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    # 分页页数显示计算
    '''
    paginator.num_pages - 对象的可分页数
    '''
    num_pages = paginator.num_pages
    '''
    paginator.page_range - 对象也的可迭代范围
    '''
    if num_pages <= 5:
        pages = paginator.page_range
    '''
    注意range的用法,range(n,m),表示n-m的范围,不包括m
    如果取最后一页,对象的可迭代范围为最后五页
    '''
    elif (num_pages - page) < 2:
        pages = [x for x in range(num_pages-4, num_pages+1)]
    '''
    如果取前两页
    对象页的可迭代范围为前五页
    '''
    elif page < 3:
        pages = [x for x in range(1, 6)]
    else:
    '''
    如果以上情况不满足,取当前page的上下两页范围
    '''
        pages = [x for x in range(page-2, page+3)]
    pre_page = page - 1
    next_page = page + 1 if page < num_pages else 0

    return render(request, 'list.html', {'sort':sort, 'type_name':GOODS_TYPE[goods_type_id], 'type_id':goods_type_id, 'new_goods_li':new_goods_li, 'goods_li':goods_li, 'cart':cart['goods_num__sum'], 'pre_page':pre_page, 'next_page':next_page, 'pages':pages, 'active_page':page})

'''
haystack是djang的全文检索插件
http://blog.csdn.net/ac_hell/article/details/52875927
'''
class MySearchView(SearchView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        for result in context['page_obj'].object_list:
            result.object.img = result.object.image_set.all()[0].img_url
        return context

