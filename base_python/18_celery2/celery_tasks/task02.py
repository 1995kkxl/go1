from celery_tasks.celery import cel
import time

@cel.task
def send_msg(name):
    print("向%s发送短信..."%name)
    time.sleep(5)
    print("向%s发送短信完成"%name)
    return "ok"