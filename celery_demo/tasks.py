from celery import shared_task


@shared_task
def add(arg1, arg2):
    print(arg1 + arg2)
    print('task.....')
    return arg1 + arg2
