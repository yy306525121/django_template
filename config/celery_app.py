import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery("django_template")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' 意味着所有的celery配置项都要有一个`CELERY_`前缀
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# task schedule define
app.conf.beat_schedule = {
    'add-every-minutes': {
        'task': 'celery_demo.tasks.add',
        # 每1分钟执行一次
        'schedule': crontab(minute='*/1'),
        'args': (10, 11)
    }
}