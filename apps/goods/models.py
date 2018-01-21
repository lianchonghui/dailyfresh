from django.db import models
from utils.models import BaseModel
from jsonfield import JSONField


class Goods(BaseModel):

    """
    商品表
    """
    YES = 1
    NO = 2
    
    ONLINE = 1
    OFFLINE = 2
    DELETED = 3

    # django的models的字段用法见注1
    goods_type_id = models.SmallIntegerField(default=1, help_text='商品分类ID')
    goods_name = models.CharField(default="", max_length=64, help_text='商品名称')
    goods_subtitle = models.CharField(default="", max_length=128, help_text='商品副标题')
    goods_price = models.FloatField(default=0.0, help_text='商品价格')
    goods_unit = models.IntegerField(default=1,help_text='商品单位')
    goods_ex_price = models.FloatField(default=0.0, help_text='商品运费')
    goods_info = models.TextField(help_text='商品描述')
    goods_status = models.IntegerField(default=ONLINE, help_text='商品状态')
    goods_stock = models.IntegerField(default=1,help_text='商品库存')
    goods_sales = models.IntegerField(default=1,help_text='商品销量')
    # django的models的内部类Meta的用法见注2
    class Meta:
        db_table = 's_goods'
'''
__repr__ 和 __str__
对象t只重写__repr___方法可以通过t, print t获取该对象信息
对象t只重写__str__方法可以通过print t获取该对象信息
对象t重写了__str__,__repr__方法,通过t获取到的是__repr__返回的信息,通过print t获取到的是__str__返回的信息
如此:__str__一般面向用户,__repr__返回的信息面向开发者
'''
    def __str__(self):
        return '%s %s' % (self.id, self.goods_name)

    '''
    @classmethod - 类方法

    objects.get()方法返回唯一一条,如果返回多条则报错
    '''
    @classmethod
    def get_one_goods(cls, goods_id):
        return cls.objects.get(id=goods_id)
    '''
    python 没有switch case语句

    objects.filter()返回0条或多条数据
    '''
    @classmethod
    def get_goods_by_type(cls, goods_type_id, limit=None, sort='default'):
        if 'price' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('goods_price')
        elif 'hot' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('-goods_sales')
        elif 'new' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('-create_time')
        else:
            data = cls.objects.filter(goods_type_id=goods_type_id)
        if None == limit:
            return data
        else:
            return data[:limit]

'''注1
http://blog.csdn.net/u014655053/article/details/72588052
model field 类型
1、AutoField
     一个自增的IntegerField，一般不直接使用，Django会自动给每张表添加一个自增的primary key。

2、BigIntegerField
    64位整数， -9223372036854775808 到 9223372036854775807。默认的显示widget 是 TextInput.

3、BinaryField （ Django 1.6 版本新增 ）
    存储二进制数据。不能使用 filter 函数获得 QuerySet

4、BooleanField
    True/False，默认的widget 是 CheckboxInput。
如果需要置空，则必须用 NullBooleanField 代替。
Django 1.6 修改：BooleanField 的默认值 由 False 改为 None，在 default 属性未设置的情况下。

5、CharField
    存储字符串。必须有 max_length 参数指定长度。默认的form widget 是 TextInput
如果字符串巨长，推荐使用 TextField。

6、CommaSeparatedIntegerField
    一串由逗号分开的整数。必须有 max_length 参数。

7、DateField
    日期，与python里的datetime.date 实例同。有以下几个可选的选项，均为bool类型：
     DateField.auto_now: 每次执行 save 操作的时候自动记录当前时间，常作为最近一次修改的时间 使用。注意：总是在执行save 操作的时候执行，无法覆盖。
 DateField.auto_now_add: 第一次创建的时候添加当前时间。常作为 创建时间 使用。注意：每次create 都会调用。
默认的form widget 是 TextInput。
注意：设置auto_now 或者 auto_now_add 为 True 会导致当前自动拥有 editable=False 和 blank = True 设置。

8、DateTimeField
    日期+时间。与python里的 datetime.datetime 实例同。常用附加选项和DateField一样。
默认 form widget 是一个 TextInput

9、DecimalField
    设置了精度的十进制数字。
A fixed-precision decimal number, represented in Python by a Decimal instance. Has two required arguments:
DecimalField.max_digits
The maximum number of digits allowed in the number. Note that this number must be greater than or equal to decimal_places.
DecimalField.decimal_places?
The number of decimal places to store with the number.
For example, to store numbers up to 999 with a resolution of 2 decimal places, you’d use:
models.DecimalField(..., max_digits=5, decimal_places=2)
And to store numbers up to approximately one billion with a resolution of 10 decimal places:
models.DecimalField(..., max_digits=19, decimal_places=10)
The default form widget for this field is a TextInput.

10、EmailField
    在 CharField 基础上附加了 邮件地址合法性验证。不需要强制设定 max_length
注意：当前默认设置 max_length 是 75，虽然已经不符合标准，但未了向前兼容，未修改。
11、FileField
    文件上传。不支持 primary_key 和 unique 选项。否则会报 TypeError 异常。
必须设置 FileField.upload_to 选项，这个是 本地文件系统路径，附加在 MEDIA_ROOT 设置的后边，也就是 MEDIA_ROOT 下的子目录相对路径。
默认的form widget 是 FileInput。
使用 FileField 和 ImageField 需要以下步骤：
    （1）修改 settting.py，设置 MEDIA_ROOT（使用绝对路径），指定用户上传的文件保存在哪里。设置 MEDIA_URL，作为 web地址 前缀，要保证 MEDIA_ROOT 目录对运行 Django 的用户是可写的；
（2）在 model 中增加 FileField 或 ImageField，并指定 upload_to 选项指定存在 MEDIA_ROOT 的哪个子目录里； 
（3）存在数据库里的是什么东西呢？是 File 或 Image相对于 MEDIA_ROOT 的相对路径，你可以在 Django 里方便的使用这个地址，比如你的 ImageField 叫 tupian，你可以在 template 中用{{object.tupian.url}}。
举个例子：假设你的 MEDIA_ROOT='/home/media'，upload_to 设置为 'photos/%Y/%m/%d'，'%Y/%m/%d' 部分使用strftime() 提供。如果你在 2013年10月10日上传了一个文件，那么它就存在 /home/media/photos/2013/10/10/ 下。
文件在 model实例 执行 save操作的同时保存，所以文件在model实例执行save之前，硬盘的上的文件名的是不可靠的。
注意：要验证用户上传的文件确实是自己需要的，以防止安全漏洞出现。
默认情况下，FileField 在数据库中表现为 varchar(100) 的一个列。你可以使用 max_length 来改变这个大小。
11、FileField 和 FieldFile
    当你访问 一个 model 内的 FileField 时，将得到一个 FieldFile 实例来访问实际的文件。这个类提供了几个属性和方法用来和实际的文件数据交互：
FieldFile.url：只读属性，获取文件的相对URL地址;
FieldFile.open( mode = 'rb' )：打开文件，和python 的 open 一样;
FieldFile.close()：和 python 的 file.close() 一样;
FieldFile.save( name, content, save=True )：name 是文件名，content 是包含了文件内容的 django.core.files.File 实例，与 python 的 file 不一样。The optional save argument controls whether or not the instance is saved after the file has been altered. Defaults to True。
两种方式 进行 content 设置：
from django.core.files import File
f = open( 'helo.txt' )
content = File(f)
另一种是：
from django.core.files.base import ContentFile
content = ContentFile( 'helloworld' )
更多内容可见：https://docs.djangoproject.com/en/dev/topics/files/
FieldFile.delete( save = True )：删除当前的文件。如果文件已经打开，则自动关闭。The optional save argument controls whether or not the instance is saved after the file has been deleted. Defaults to True.
值得注意的是：当一个 model实例 被删除之后，相关联的文件并没有被删除，需要自己清除！

12、FloatField
    与 python 里的 float 实例相同，默认的 form widget 是 TextInput。
虽然 FloatField 与 DecimalField 都是表示实数，但却是不同的表现形式，FloatField 用的是 python d float 类型，但是 DecimalField 用的却是 Decimal 类型。区别可见：http://docs.python.org/2.7/library/decimal.html#decimal
13、ImageField
    在 FileField 基础上加上是否是合法图片验证功能的一个类型。
除了 FileField 有的属性外，ImageField 另有 height 和 width 属性。
To facilitate querying on those attributes, ImageField has two extra optional arguments:

ImageField.height_field
Name of a model field which will be auto-populated with the height of the image each time the model instance is saved.

ImageField.width_field
Name of a model field which will be auto-populated with the width of the image each time the model instance is saved.

注意：需要安装 PIL 或者 Pillow 模块。在数据库中同样表现为 varchar(100)，可通过 max_length 改大小。
14、IntegerField
    整数，默认的form widget 是 TextInput。
15、IPAddressField
    IP地址，字符串类型，如 127.0.0.1。默认 form widget 是 TextInput。
16、TextField
    大文本，巨长的文本。默认的 form widget 是 Textarea。
注意，如果使用 MySQLdb 1.2.1p2 和 utf-8_bin 编码，会有一些问题https://docs.djangoproject.com/en/dev/ref/databases/#mysql-collation。具体问题未分析，可自行避开。
17、URLField
    加了 URL 合法性验证的 CharField。
默认的 form widget 是 TextInput。
默认max_length=200，可修改。
18、ForeignKey / ManyToManyField / OneToOneField / SmallIntegerField / SlugField / PositiveSmallIntegerField / PositiveIntegerField

Field 选项

null
      boolean 值，缺省设置为false。通常不将其用于字符型字段上，比如CharField，TextField上。字符型字段如果没有值会返回空字符串。

blank
      boolean 值，该字段是否可以为空。如果为假，则必须有值。

choices
     元组值，一个用来选择值的2维元组。第一个值是实际存储的值，第二个用来方便进行选择。如SEX_CHOICES=((‘F’,’Female’),(‘M’,’Male’),)

db_column
      string 值，指定当前列在数据库中的名字，不设置，将自动采用model字段名；
db_index 
      boolean 值，如果为True将为此字段创建索引；

default
      给当前字段设定的缺省值，可以是一个具体值，也可以是一个可调用的对象，如果是可调用的对象将每次产生一个新的对象；

editable
      boolean 值，如果为假，admin模式下将不能改写。缺省为真；

error_messages
      字典，设置默认的出错信息，可覆盖的key 有 null, blank, invalid, invalid_choice, 和 unique。

help_text
      admin模式下帮助文档
      form widget 内显示帮助文本。
primary_key
      设置主键，如果没有设置django创建表时会自动加上：id = meta.AutoField(‘ID’, primary_key=True)
      primary_key=True implies blank=False, null=False and unique=True. Only one primary key is allowed on an object.

radio_admin
      用于 admin 模式下将 select 转换为 radio 显示。只用于 ForeignKey 或者设置了choices

unique
      boolean值，数据是否进行唯一性验证；
unique_for_date
      字符串类型，值指向一个DateTimeField 或者 一个 DateField的列名称。日期唯一，如下例中系统将不允许title和pub_date两个都相同的数据重复出现
      title = meta.CharField( maxlength=30, unique_for_date=’pub_date’ )

unique_for_month / unique_for_year
      用法同上

verbose_name
      string类型。更人性化的列名。

validators
        有效性检查。无效则抛出 django.core.validators.ValidationError 异常。
如何实现检查器 见：https://docs.djangoproject.com/en/dev/ref/validators/

on_delete级联删除
在一对多关系中，例如主机对应多个role,每个role对应1个主机，
当删除了某个主机时候，发现对应的role也被删除了，于是查了手册，应该如下写：

class Host(models.Model):  
    hostname = models.CharField(max_length=20,primary_key=True, blank=False)  
    static_ip = models.CharField(max_length=20,unique = True)  
  
class CCRole(models.Model):  
    name = models.CharField(max_length = 20,primary_key = True)  
    host = models.ForeignKey(Host,null=True,blank=True,on_delete=models.SET_NULL)  
给ForeignKey增加属性，
on_delete=models.SET_NULL
即可。

该属性还有其他值可选：
CASCADE: 默认的，级联删除
PROTECT: 通过抛出django.db.models.ProtectedErrordjango.db.models.ProtectedError错误来阻止删除关联的对象 
SET_NULL: 设置ForeignKey 为 null; 这个只有设置了null 为 True的情况才能用
SET_DEFAULT: 设置 ForeignKey 为默认值; 默认值必须预先设置
SET(): 设置为某个方法返回的值
DO_NOTHING: 什么都不做，如果数据库设置必须关联则会报IntegrityError错。
'''

'''注2
Django models中的meta选项
通过一个内嵌类 "class Meta" 给你的 model 定义元数据, 类似下面这样:

class Foo(models.Model): 
    bar = models.CharField(maxlength=30)

    class Meta: 
        # ...
Model 元数据就是 "不是一个字段的任何数据" -- 比如排序选项, admin 选项等等.

下面是所有可能用到的 Meta 选项. 没有一个选项是必需的. 是否添加 class Meta 到你的 model 完全是可选的.

app_label
app_label这个选项只在一种情况下使用，就是你的模型类不在默认的应用程序包下的models.py文件中，这时候你需要指定你这个模型类是那个应用程序的。比如你在其他地方写了一个模型类，而这个模型类是属于myapp的，那么你这是需要指定为：

app_label='myapp'
db_table
db_table是用于指定自定义数据库表名的。Django有一套默认的按照一定规则生成数据模型对应的数据库表名，如果你想使用自定义的表名，就通过这个属性指定，比如：

db_table='my_owner_table'   
若不提供该参数, Django 会使用 app_label + '_' + module_name 作为表的名字.

若你的表的名字是一个 SQL 保留字, 或包含 Python 变量名不允许的字符--特别是连字符 --没关系. Django 会自动在幕后替你将列名字和表名字用引号引起来.

db_tablespace
有些数据库有数据库表空间，比如Oracle。你可以通过db_tablespace来指定这个模型对应的数据库表放在哪个数据库表空间。

get_latest_by
由于Django的管理方法中有个lastest()方法，就是得到最近一行记录。如果你的数据模型中有 DateField 或 DateTimeField 类型的字段，你可以通过这个选项来指定lastest()是按照哪个字段进行选取的。

一个 DateField 或 DateTimeField 字段的名字. 若提供该选项, 该模块将拥有一个 get_latest() 函数以得到 "最新的" 对象(依据那个字段):

get_latest_by = "order_date"
managed
由于Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False。

默认值为True,这个选项为True时Django可以对数据库表进行 migrate或migrations、删除等操作。在这个时间Django将管理数据库中表的生命周期

如果为False的时候，不会对数据库表进行创建、删除等操作。可以用于现有表、数据库视图等，其他操作是一样的。

order_with_respect_to
这个选项一般用于多对多的关系中，它指向一个关联对象。就是说关联对象找到这个对象后它是经过排序的。指定这个属性后你会得到一个get_XXX_order()和set_XXX_order（）的方法,通过它们你可以设置或者回去排序的对象。

举例来说, 如果一个 PizzaToppping 关联到一个 Pizza 对象, 这样做:

order_with_respect_to = 'pizza'
...就允许 toppings 依照相关的 pizza 来排序.

ordering
这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。比如下面的代码：

ordering=['order_date'] 
# 按订单升序排列
ordering=['-order_date'] 
# 按订单降序排列，-表示降序
ordering=['?order_date'] 
# 随机排序，？表示随机
ordering = ['-pub_date', 'author']
# 对 pub_date 降序,然后对 author 升序
需要注意的是:不论你使用了多少个字段排序, admin 只使用第一个字段

permissions
permissions主要是为了在Django Admin管理模块下使用的，如果你设置了这个属性可以让指定的方法权限描述更清晰可读。

要创建一个对象所需要的额外的权限. 如果一个对象有 admin 设置, 则每个对象的添加,删除和改变权限会人(依据该选项)自动创建.下面这个例子指定了一个附加权限: can_deliver_pizzas:

permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)
这是一个2-元素 tuple 的tuple或列表, 其中两2-元素 tuple 的格式为:(permission_code, human_readable_permission_name).

unique_together
unique_together这个选项用于：当你需要通过两个字段保持唯一性时使用。这会在 Django admin 层和数据库层同时做出限制(也就是相关的 UNIQUE 语句会被包括在 CREATE TABLE 语句中)。比如：一个Person的FirstName和LastName两者的组合必须是唯一的，那么需要这样设置：

unique_together = (("first_name", "last_name"),)
verbose_name
verbose_name的意思很简单，就是给你的模型类起一个更可读的名字：

verbose_name = "pizza"
若未提供该选项, Django 则会用一个类名字的 munged 版本来代替: CamelCase becomes camel case.

verbose_name_plural
这个选项是指定，模型的复数形式是什么，比如：

verbose_name_plural = "stories"
若未提供该选项, Django 会使用 verbose_name + "s".
'''