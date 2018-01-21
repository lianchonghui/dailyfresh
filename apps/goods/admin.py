from django.contrib import admin
from apps.goods.models import *

'''Django Admin管理工具
http://www.runoob.com/django/django-admin-manage-tool.html
http://python.usyiyi.cn/translate/django_182/ref/contrib/admin/index.html
list_display 列表显示的字段
serch_filds 搜索栏可搜索的字段
list_filter 设置激活激活Admin 修改列表页面右侧栏中的过滤器
'''
# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
	list_display = ('goods_type_id', 'goods_name','goods_subtitle', 'goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales')
	search_fields = ('goods_type_id', 'goods_name','goods_subtitle','goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales')
	list_filter = ['goods_type_id', 'goods_name','goods_subtitle','goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales']

admin.site.register(Goods,GoodsAdmin)
