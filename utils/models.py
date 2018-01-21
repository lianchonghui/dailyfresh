from django.db import models
from jsonfield import JSONField
import copy
from django.utils import timezone
from .logics import model_to_dict


class BaseModel(models.Model):

    """
    所有类的基类
    """

    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间')
    extinfo = JSONField(
        blank=True, null=True, default={}, help_text='扩展字段')

    class Meta:
        abstract = True

    def canonical(self, exclude=None):
        return model_to_dict(self, exclude)

    @classmethod
    def add_one_object(cls, **kwargs):
        """ 添加一个新的实例
        """
        '''
        _get_all_valid_fields()自定义类方法,返回该model的有效字段的tuple
        '''
        valid_fields = cls._get_all_valid_fields()
        '''
        拷贝kwargs,对副本循环来操作kwargs
        '''
        kws = copy.copy(kwargs)
        extinfo = dict()
        for k, v in kws.items():
            '''
            剔除非有效字段,并记录在extinfo字典中
            '''
            if k not in valid_fields:
                extinfo[k] = v
                kwargs.pop(k)
        '''
        对于参数中包含extinfo,则如果是字典,则更新到现有的extinfo中,如果不是字典则剔除
        '''
        if 'extinfo' in kwargs:
            if isinstance(kwargs['extinfo'], dict):
                extinfo.update(kwargs.get('extinfo'))
            else:
                kwargs.pop('extinfo')
        kwargs.update(extinfo=extinfo)
        '''
        判断create_time是否为有效字段,如果是,则添加到当前参数中,避免每次新增自己指定create_time
        '''

        if 'create_time' in valid_fields:
            kwargs.update(create_time=timezone.now())
        obj = cls(**kwargs)
        obj.save()
        return obj

    @classmethod
    def get_one_object(cls, filters):
        obj = cls.objects.get(**filters)
        return obj

    @classmethod
    def _get_all_valid_fields(cls):
        '''
        判断该类是否为ModelBase类型
        '''
        if not isinstance(cls, models.base.ModelBase):
            return tuple()
        '''
        get_all_field_names()
        返回当前model类的所有字段名称
        '''
        return set(cls._meta.get_all_field_names())
    '''
    自定义的查询类方法
    filters - filter参数
    exclude_filters - exclude参数
    order_by - order_by参数,默认以pk倒序
    values - values参数,values='列名',获取该列的数据,返回的是ValuesQuerySet,是QuerySet 的子类,注意不是list
    '''
    @classmethod
    def get_object_list(cls, filters={}, exclude_filters={},
                        order_by=('-pk', ), values=None,
                        page_index=None, page_size=None):
        """ 获取对象列表
        """
        objs = cls.objects.filter(**filters)\
                  .exclude(**exclude_filters)\
                  .order_by(*order_by)
        if values:
            objs = objs.values(*values)

        '''
        可以替换为
        all((page_index,page_size))
        None即为False
        '''
        if all(map(lambda x: x is not None, (page_index, page_size))):
            start = page_index * page_size
            end = start + page_size
            objs = objs[start: end]
        return objs
