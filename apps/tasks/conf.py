from celery import Celery

'''
http://docs.celeryproject.org/en/master/getting-started/first-steps-with-celery.html
http://student-lp.iteye.com/blog/2093397
http://python.jobbole.com/87238/
http://blog.nsfocus.net/celery-asynchronous-task/
http://blog.csdn.net/kk123a/article/details/74549117
'''
class CeleryConf(object):
    BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('apps.tasks.tasks')

'''
1.创建一个Celery对象,第一个参数为celery名称
2.config_from_object() - 配置Celery参数为一个对象或者模块名
3.在tasks中使用@app.task装饰器包装函数为worker
4.使用被包装函数的delay触发worker
'''
app = Celery('apps.tasks.conf')
app.config_from_object(CeleryConf)
