#encoding=utf-8
"""
Django settings for dailyfresh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
'''
项目的根目录
    先获取到settings.py的所在目录
    再获取到该目录的所在目录即是项目根目录
'''
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1%_z=5p@j8lz*9cxfh3p-u@6j7aam@i!4vg2kg$h((94_i7z!1'
'''
# 密钥配置
# 适用于开发环境和部署环境
# 可以从系统环境中，配置文件中，和硬编码的配置中得到密钥
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except:
    try:
        with open(os.path.join(PROJECT_ROOT, 'db/secret_key').replace('\\', '/')) as f:
            SECRET_KEY = f.read().strip()
    except:
        SECRET_KEY = '*lk^6@0l0(iulgar$j)faff&^(^u+qk3j73d18@&+ur^xuTxY'
'''

'''
是否开启debug模式
'''
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

'''
一个布尔值,用来开关模板调试模式.若设置为 True, 如果有任何 TemplateSyntaxError,
一个详细的错误报告信息页将被显示给你.这个报告包括有关的模板片断,相应的行会自动高亮
'''
TEMPLATE_DEBUG = True

'''
限制访问域名
'''
# ALLOWED_HOSTS = ['*'] # 任意域名皆可访问
ALLOWED_HOSTS = []


# Application definition

'''
注册app
'''
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'apps.passport',
    'apps.profile',
    'apps.goods',
    'apps.image',
    'apps.cart',
    'apps.order',
    'apps.address',
)

'''
一个django 用到的中间件 class 名称的 tuple. 参阅 middleware 文档.
'''
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.middlewares.UtilMiddleWare',
)

'''
指定根路由
'''
ROOT_URLCONF = 'dailyfresh.urls'

'''
指定wsgi
'''
WSGI_APPLICATION = 'dailyfresh.wsgi.application'

'''
django自带用户登录检验跳转配置
    1.view 方法的前面添加 django 自带的装饰器 @login_required
    2.在settings.py中配置LOGIN_URL(该地址即为跳转到的登录界面)
'''
LOGIN_URL = '/passport/login'

'''
数据库配置
'''
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

'''
设置STATIC_URL为存储静态文件的路径（基于根目录） 
静态文件目录css,js,images等
'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

'''
TEMPLATE_DIRS模板目录,即html或其他网页模板所在目录,在views.py中的渲染使用的模板在这个文件夹下查找
    这是个list,可以有多个模板目录
'''
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [
    TEMPLATE_PATH,
]

'''
STATICFILES_DIRS    
一般放置除了各个app的其他公共的静态资源路径
配置存储静态文件的路径映射值，这个值用于模版引用路径的转换
'''
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

'''关于静态文件在模板的引用
1、在settings.py中加入静态文件的定义
STATIC_URL = '/static/' //设置STATIC_URL为存储静态文件的路径（基于根目录）  

STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, "static"),  
)  
  
//  配置存储静态文件的路径映射值，这个值用于模版引用路径的转换  
2. 在urls.py中添加静态文件请求的路径映射

url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),  

3、在模版文件中引用

{% load staticfiles %}  
//  模版文件中需要引用staticfiles，如果未加这句引用的话，模版引用找不到static符号  

<img src="{% static "xx.png"%}"></img>  
//   静态文件引用方式  
'''

'''
MEDIA_ROOT默认值: '' (空的字符串)

一个绝对路径, 用于保存媒体文件. 例子: "/home/media/media.lawrence.com/" 参阅 MEDIA_URL.

MEDIA_URL默认值: '' (空的字符串)

处理媒体服务的URL(媒体文件来自 MEDIA_ROOT). 如: "http://media.lawrence.com"

models.py中的up_load属性会上传到MEDIR_ROOT下
'''
MEDIA_URL = '/static/res/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/res')

'''
指定语言编码
'''
LANGUAGE_CODE = 'zh_CN'

'''
指定时区
'''
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


'''
覆盖django自带的USER模型
使用自定义的用户模型
https://www.jianshu.com/p/b993f4feff83
'''
AUTH_USER_MODEL = 'passport.Passport'

'''
使用djang邮件模块
from django.core.mail import send_mail  
django EMIAL各项配置
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '*****@qq.com'
EMAIL_HOST_PASSWORD = 'fuetnskqacerbgfh'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

'''
haystack是djang的全文检索插件
http://blog.csdn.net/ac_hell/article/details/52875927
'''
# haystack + elasticsearch
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'ecom_haystack',
        'TIMEOUT': 60
    },
}
#索引自动更新
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


'''
# redis 安装redis插件$ pip install django-redis
# http://blog.csdn.net/bugall/article/details/43956445
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "CONNECTION_POOL_KWARGS": {"max_connections": 100}, # 对于高并发的连接池配置
        }
    }
}
# 读写操作
#from django.conf import settings
#from django.core.cache import cache
# cache.set('get_user_id_bugall',123,settings.NEVER_REDIS_TIMEOUT)
# cache.get('get_user_id_bugall');

'''

'''
http://blog.163.com/stu_shl/blog/static/59937509201192012536637/
setting.py

          这个文件包含了所有有关这个Django项目的配置信息，均大写：   TEMPLATE_DIRS , DATABASE_NAME , 等. 最重要的设置是 ROOT_URLCONF，它将作为 URLconf 告诉 Django 在这个站点中那些 Python的模块将被用到。

          使用 Django 时, 你必须告诉它你使用的是哪个 settings . 要做到这一点，使用环境变量DJANGO_SETTINGS_MODULE.

默认 settings
在manage.py中指定
       如果不需要, Django settings 文件可以不必定义任何 settings. 因为每个设置都有默认值. 这些默认值定义在django/conf/global_settings.py.

使用 settings 的法则:

从 global_settings.py 载入默认设置. 
从指定的 settings 文件载入用户设置, 需要时覆盖掉默认设置.注意一个用户 settings 文件，不必导入 global_settings, 这是多余的.

查看你改变了哪些设置
有一个简单的办法可以查看你修改了哪些设置.命令 python manage.py diffsettings 显示当前 settings 文件与Django 默认设置的不同之处.

在你的代码中使用 settings
通过从模块 django.conf.settings 导入你需要的变量, 你的代码可以访问这个变量. 例子:

from django.conf.settings import DEBUG

if DEBUG:
                  # Do something
注意一定 不要 从 global_settings 或你自己的 settings 模块导入设置变量到你的代码. django.conf.settings 概括了默认设置和站点自定义设置的概念,它提供了一个统一的接口用于用户代码访问, 也降低了用户代码与用户设置的耦合程度.

在运行时修改 settings
         不应该在程序运行时修改 settings. 举例来说, 不要在一个 view 中做这样的事:

                       from django.conf.settings import DEBUG

                        DEBUG = True   # Don't do this!
      你只应该在你的 settings 文件中设置 settings, 记住,这是原则.

安全性
由于 settings 文件包含敏感信息,象数据库密码等.你应该非常小心的设置它的访问权限. 举例来说, 你可以只允许你和 WEB 服务器用户阅读该文件.在一个共享主机环境时,这一点格外重要.

可用选项

下面是所有可用选项的列表及它们的默认值(按字母顺序排列).

ABSOLUTE_URL_OVERRIDES        默认值: {} (空字典)

一个字典映射 "app_label.module_name" 字符串到一个函数, 该函数接受一个model对象作为参数并返回它的URL. 这是在一个安装上覆盖 get_absolute_url() 方法的一种方式. 例子:

ABSOLUTE_URL_OVERRIDES =

{
    'blogs.blogs': lambda o: "/blogs/%s/" % o.slug,
    'news.stories': lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
        }
           ADMIN_FOR            默认值: () (空的tuple)

用于 admin-site settings 模块, 若当前站点是 admin ,它则是一个由 settings 模块组成的 tuple (类似'foo.bar.baz' 这样的格式).

admin 站点在 models, views,及 template tags 的自动内省的文档中使用该设置.

ADMIN_MEDIA_PREFIX 默认值: '/media/'

The URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a trailing slash.

ADMINS                     默认值: () (空的 tuple)

一个2-元素tuple的 tuple. 列出了有权接收代码错误提示的人. 当 DEBUG=False 时,一个 view 引发了异常, Django 会将详细异常信息用电子邮件的方式发送给这些人. 该tuple的每个成员应该是这种格式: (Full name, e-mail address). 例子:

(('John','john@example.com'), ('Mary','mary@example.com'))
      ALLOWED_INCLUDE_ROOTS        默认值: () (空的 tuple)

一个字符串tuple, 只有以列表中的元素为前缀的模板Django才可以以``{% ssi %}`` 形式访问 . 出于安全考虑, 在不应该访问时,即使是模板的作者也不能访问这些文件.

举例来说, 若 ALLOWED_INCLUDE_ROOTS 是 ('/home/html', '/var/www'), 那么 {% ssi /home/html/foo.txt %} 可以正常工作, 不过 {% ssi /etc/passwd %} 却不能.

APPEND_SLASH 默认值: True

是否给URL添加一个结尾的斜线. 只有安装了 CommonMiddleware 之后,该选项才起作用. (参阅 middleware 文档). 参阅 PREPEND_WWW.

CACHE_BACKEND默认值: 'simple://'

后端使用的 cache . 参阅 cache docs.

CACHE_MIDDLEWARE_KEY_PREFIX默认值: '' (空的字符串)

cache 中间件使用的cache key 前缀. 参阅 cache docs.

DATABASE_ENGINE默认值: 'postgresql'

后端使用的数据库引擎: 'postgresql', 'mysql', 'sqlite3' 或 'ado_mssql' 中的任意一个.

DATABASE_HOST默认值: '' (空的字符串)

数据库所在的主机. 空的字符串意味着 localhost. SQLite 不需要该项. 如果你使用 MySQL 并且该选项的值以一个斜线 ('/') 开始, MySQL 则通过一个 Unix socket 连接到指定的 socket. 比如:

DATABASE_HOST = '/var/run/mysql'
如果你使用 MySQL 并且该选项的值 不是 以斜线开始, 那么该选项的值就是主机的名字.

DATABASE_NAME默认值: '' (空的字符串)

要使用的数据库名字. 对 SQLite, 它必须是一个数据库文件的全路径名字.

DATABASE_PASSWORD默认值: '' (空的字符串)

连接数据库需要的密码. SQLite 不需要该项.

DATABASE_PORT默认值: '' (空的字符串)

连接数据库所需的数据库端口. 空的字符串表示默认端口. SQLite 不需要该项.

DATABASE_USER默认值: '' (空的字符串)

连接数据库时所需要的用户名. SQLite 不需要该项.

DATE_FORMAT默认值: 'N j, Y' (举例来说 Feb. 4, 2003)

在 Django admin change-list 页对日期字段使用的默认日期格式, 系统中的其它部分也可能使用该格式. 参阅allowed date format strings.

参阅 DATETIME_FORMAT 和 TIME_FORMAT.

DATETIME_FORMAT
默认值: 'N j, Y, P' (举例来说 Feb. 4, 2003, 4 p.m.)

在 Django admin change-list 页对日期时间字段使用的默认日期时间格式, 系统中的其它部分也可能使用该格式. 参阅 allowed date format strings.

参阅 DATE_FORMAT 和 TIME_FORMAT.

DEBUG默认值: False

一个开关调试模式的逻辑值

DEFAULT_CHARSET默认值: 'utf-8'

如果一个 MIME 类型没有人为指定, 对所有 HttpResponse 对象将应用该默认字符集. 使用DEFAULT_CONTENT_TYPE 来构建 Content-Type 头.

DEFAULT_CONTENT_TYPE默认值: 'text/html'

如果一个 MIME 类型没有人为指定, 对所有 HttpResponse 对象将应用该默认 content type. 使用DEFAULT_CHARSET 来构建 Content-Type 头.

DEFAULT_FROM_EMAIL默认值: 'webmaster@localhost'

用于发送(站点自动生成的)管理邮件的默认 e-mail 邮箱.

DISALLOWED_USER_AGENTS默认值: () (空的 tuple)

一个编译的正则表达式对象列表,用于表示一些用户代理字符串.这些用户代理将被禁止访问系统中的任何页面. 使用这个对付页面机器人或网络爬虫.只有安装 CommonMiddleware 后这个选项才有用(参阅 middleware 文档).

EMAIL_HOST默认值: 'localhost'

用来发送 e-mail 的主机. 参阅 EMAIL_PORT.

EMAIL_HOST_PASSWORD默认值: '' (空的字符串)

EMAIL_HOST 中定义的 SMTP 服务器使用的密码. 如果为空, Django 不会尝试进行认证.

参阅 EMAIL_HOST_USER.

EMAIL_HOST_USER默认值: '' (空的字符串)

EMAIL_HOST 中定义的 SMTP 服务器使用的用户名. 如果为空, Django 不会尝试进行认证.

参阅 EMAIL_HOST_PASSWORD.

EMAIL_PORT默认值: 25

EMAIL_HOST 中指定的SMTP 服务器所使用的端口号.

EMAIL_SUBJECT_PREFIX默认值: '[Django] '

django.core.mail.mail_admins 或 django.core.mail.mail_managers 发送的邮件的主题前缀.

ENABLE_PSYCO默认值: False

如果允许 Psyco, 将使用Pscyo优化 Python 代码. 需要 Psyco 模块.

IGNORABLE_404_ENDS默认值: ('mail.pl', 'mailform.pl', 'mail.cgi', 'mailform.cgi', 'favicon.ico', '.php')

参阅 IGNORABLE_404_STARTS.

IGNORABLE_404_STARTS默认值: ('/cgi-bin/', '/_vti_bin', '/_vti_inf')

一个字符串 tuple . 以该tuple中元素为开头的 URL 应该被 404 e-mailer 忽略. 参阅SEND_BROKEN_LINK_EMAILS 和 IGNORABLE_404_ENDS.

INSTALLED_APPS默认值: () (空的 tuple)

一个字符串tuple ,内容是本 Django 安装中的所有应用. 每个字符串应该是一个包含Django应用程序的Python包的路径全称, django-admin.py startapp 会自动往其中添加内容.

INTERNAL_IPS默认值: () (空的 tuple)

一个 ip 地址的 tuple(字符串形式), 它:

当 DEBUG 为 True 时,参阅调试务注解
接收 X 头(若 XViewMiddleware 已安装), (参阅 middleware 文档) 
JING_PATH
默认值: '/usr/bin/jing'

"Jing" 执行文件路径全名. Jing 是一个 RELAX NG 校验器, Django 使用它对你的 model 的 XMLField 进行验证. 参阅 http://www.thaiopensource.com/relaxng/jing.html .

LANGUAGE_CODE默认值: 'en-us'

表示默认语言的一个字符串. 必须是标准语言格式. 举例来说, U.S. English 就是 "en-us". 参阅internationalization docs.

LANGUAGES默认值: 一个 tuple (内容为所有可用语言). 目前它的值是:

LANGUAGES = (
    ('bn', _('Bengali')),
    ('cs', _('Czech')),
    ('cy', _('Welsh')),
    ('da', _('Danish')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('gl', _('Galician')),
    ('is', _('Icelandic')),
    ('it', _('Italian')),
    ('no', _('Norwegian')),
    ('pt-br', _('Brazilian')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('sr', _('Serbian')),
    ('sv', _('Swedish')),
    ('zh-cn', _('Simplified Chinese')),
)
一个2-元素tuple<格式为 (语言代码, 语言名称)>的 tuple. 该设置用于选择可用语言.参阅internationalization docs 了解细节.

通常这个默认值就足够了.除非你打算减少提供的语言数目,否则没必要修改这个设置.

MANAGERS默认值: ADMINS (不论 ADMINS 是否已经设置)

一个和 ADMINS 同样格式的 tuple , 当 SEND_BROKEN_LINK_EMAILS=True 时, 这些人有权接收死链接通知信息.

MEDIA_ROOT默认值: '' (空的字符串)

一个绝对路径, 用于保存媒体文件. 例子: "/home/media/media.lawrence.com/" 参阅 MEDIA_URL.

MEDIA_URL默认值: '' (空的字符串)

处理媒体服务的URL(媒体文件来自 MEDIA_ROOT). 如: "http://media.lawrence.com"

MIDDLEWARE_CLASSES
        默认值:

("django.contrib.sessions.middleware.SessionMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.doc.XViewMiddleware")
一个django 用到的中间件 class 名称的 tuple. 参阅 middleware 文档.

PREPEND_WWW默认值: False

是否为没有 "www." 前缀的域名添加 "www." 前缀. 当且仅当安装有 CommonMiddleware 后该选项才有效. (参阅middleware 文档).参阅 APPEND_SLASH.

ROOT_URLCONF默认值: Not defined

一个字符串,表示你的根 URLconf 的模块名. 举例来说:"mydjangoapps.urls". 参阅 Django如何处理一个请求.

SECRET_KEY默认值: '' (空的字符串)

一个密码. 用于为密码哈希算法提供一个种子.将其设置为一个随机字符串 -- 越长越好. django-admin.py startproject 会自动给你创建一个.

SEND_BROKEN_LINK_EMAILS默认值: False

当有人从一个有效Django-powered页面访问另一个Django-powered页面时发现404错误(也就是发现一个死链接)时, 是否发送一封邮件给 MANAGERS. 当且仅当 安装有 CommonMiddleware 时该选项才有效(参阅`middleware 文档`_). 参阅 IGNORABLE_404_STARTS `` 和 IGNORABLE_404_ENDS``.

SERVER_EMAIL默认值: 'root@localhost'

用来发送错误信息的邮件地址, 比如发送给 ADMINS 和 MANAGERS 的邮件.

SESSION_COOKIE_AGE默认值: 1209600 (2周, 以秒计)

session cookies 的生命周期, 以秒计. 参阅 session docs.

SESSION_COOKIE_DOMAIN默认值: None

session cookies 有效的域. 将其值设置为类似 ".lawrence.com" 这样 cookie 就可以跨域生效, 或者使用None 作为一个标准的域 cookie. 参阅 session docs.

SESSION_COOKIE_NAME默认值: 'sessionid'

session 使用的cookie 名字. 参阅 session docs.

SESSION_SAVE_EVERY_REQUEST默认值: False

是否每次请求都保存session. 参阅 session docs.

SITE_ID默认值: Not defined

是一个整数, 表示 django_site 表中的当前站点. 当一个数据包含多个站点数据时，你的程序可以据此 ID 访问特定站点的数据．

TEMPLATE_CONTEXT_PROCESSORS默认值:

("django.core.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n")
A tuple of callables that are used to populate the context in RequestContext. These callables take a request object as their argument and return a dictionary of items to be merged into the context.

TEMPLATE_DEBUG默认值: False

一个布尔值,用来开关模板调试模式.若设置为 True, 如果有任何 TemplateSyntaxError,一个详细的错误报告信息页将被显示给你.这个报告包括有关的模板片断,相应的行会自动高亮.

注意 Django 仅在 DEBUG 为 True 时显示这个信息页面.

参阅 DEBUG.

TEMPLATE_DIRS默认值: () (空的 tuple)

模板源文件目录列表,按搜索顺序. 注意要使用 Unix-风格的前置斜线(即'/'), 即便是在 Windows 上.

参阅 template documentation.

TEMPLATE_LOADERS默认值: ('django.template.loaders.filesystem.load_template_source',)

一个元素为可调用对象(字符串形式的)的 tuple. 这些对象知道如何导入 templates 从各种源中. 参阅 template documentation.

TEMPLATE_STRING_IF_INVALID默认值: '' (空的字符串)

输出文本, 作为一个字符串. 模板系统将会在出错 (比如说拼错了) 时使用该变量. 参阅 How invalid variables are handled.

TIME_FORMAT默认值: 'P' (举例来说 4 p.m.)

Django admin change-list 使用的默认时间格式. 有可能系统的其它部分也使用该格式. 参阅 allowed date format strings.

参阅 DATE_FORMAT 和 DATETIME_FORMAT.

TIME_ZONE默认值: 'America/Chicago' (我们可以用 'Asia/Shanghai PRC' )

一个表示当前时区的字符串. 参阅 选择项列表.

Django 据此设置转换所有的日期/时间 -- 并不考虑服务器的时区设置. 举例来说, 一台服务器可以服务多个Django-powered 站点,每个站点使用一个独立的时区设置.

USE_ETAGS默认值: False

一个布尔值.指定是否输出 "Etag" 头. 这个选项可以节省网络带宽,但损失性能. 只有安装 CommonMiddleware 后这个选项才有用(参阅 middleware 文档)

创建你自己的 settings
         你可以为自己的Django 应用程序创建自定义 settings. 只需要你遵守以下惯例:

      设置名称全部大写. 如果某项设置是一个序列,优先使用 tuple.这完全是基于性能考虑. 不要为已经存的一个设置重新发明一个名字. 
'''