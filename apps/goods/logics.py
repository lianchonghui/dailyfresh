import json
from .models import Goods
from .enums import *

'''
商品逻辑
对dao层返回的数据进行处理和封装
'''
class GoodsLogic(object):

    """
    商品逻辑
    """

    @classmethod
    def get_one_goods(cls, goods_id):
        '''
        调用dao层方法获取元数据
        '''
        data = Goods.get_one_goods(goods_id)
        '''
        对数据进行格式化处理
        '''
        data.price = "%.2f" % data.goods_price
        data.img = data.image_set.all()[0].img_url
        '''
        通过枚举数据获取id对应的名称,减少数据库的存储,避免名称的修改需要更新数据库
        '''
        data.type_name = GOODS_TYPE[data.goods_type_id]
        return data


    @classmethod
    def get_goods_by_type(cls, goods_type_id, limit=None, sort='default'):
        data = Goods.get_goods_by_type(goods_type_id, limit, sort)
        for i in data:
            i.price = "%.2f" % i.goods_price
            '''
            image_set关联表查询方式:表名_set
            '''
            i.img = i.image_set.all()[0].img_url
        return data

'''https://www.cnblogs.com/zhaopengcheng/p/5608328.html?utm_source=tuicool&utm_medium=referral
两张通过外键联系的表，如何在一张表上根据另一张表上的属性查找满足条件的对象集？

 平常查找表中数据的条件是python中已有的数据类型，通过名字可以直接查找。如果条件是表中外键列所对应表的某一列，该如何查询数据？

表1是新闻表，是回复表中某一外键指向的表，表2是回复表。

问题1：根据表1的某些条件来查找表2的对象集。

复制代码
class News(models.Model):
    title = models.CharField(max_length=50);
    summary = models.TextField();
    
    url = models.CharField(max_length=150);
    favorCount = models.IntegerField(default=0);
    favorUsername = models.TextField(default="");
    replyCount = models.IntegerField(default=0);

class Reply(models.Model):
    content = models.TextField();
    user = models.ForeignKey('User');
    newID = models.ForeignKey('News');
    replyTime = models.DateTimeField(auto_now_add=True);
    
    def __unicode__(self):
        return self.content;
复制代码
像这样的数据表，想要查找对于新闻id是3的所有回复？

方法一、首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据。

obj = models.News.objects.get(id=3)
replys = obj.reply_set.all()
方法二、直接在目标表中通过双下划线来指定外键对应表中的域来查找符合条件的对象。

models.Reply.objects.filter(newID__id=3)
mdoles.Reply.objects.filter(newID__title='xxx')
 

问题2： 根据表2的某些条件查找表1的对象集。此时需要将表2的名字小写加两个下划线，再加上查找条件。比如：查找回复内容中包含“new”的所有新闻

models.News.objects.filter(reply__content__contains='new');
__contains是模糊查询,一般是一个_,此处是__两个
在filter中可以这样用，在values方法中也可以这样使用，此时的值便是外键对应表中的数据。
'''
