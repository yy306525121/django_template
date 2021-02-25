Django模板项目


# 用户名密码
admin用户名:yzy  密码:123456


# Celery


## 启动celery任务
    celery -A config.celery_app worker -l info

# Celery schedule
## Crontab schedules
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
### 使用
* 在celery_demo.tasks中添加任务
```python
@shared_task
def add(arg1, arg2):
    print(arg1 + arg2)
    print('task.....')
    return arg1 + arg2
```

* 在config.celery_app中添加定时配置
```python
app.conf.beat_schedule = {
    'add-every-minutes': {
        'task': 'celery_demo.tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (10, 11)
    }
}
```
  
### 启动 celery schedule 服务
    celery -A config.celery_app beat`