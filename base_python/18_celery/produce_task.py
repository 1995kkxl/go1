# from celery_task import send_email,send_msg
#
# #消费者
#
# result = send_email.delay("yuan")
# print(result.id)
# result2 = send_msg.delay("alex")
# print(result2.id)


#----定时任务执行
from celery_task import send_email
from datetime import datetime

#方式一
# v1 = datetime(2020, 6, 10, 19, 43, 00)
# print(v1) #时间搓
# v2 = datetime.utcfromtimestamp(v1.timestamp())
# print(v2)
# result = send_email.apply_async(args=["egon",], eta=v2) ##args参数
# print(result.id)


# 方式二
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta
time_delay = timedelta(seconds=10) #10秒钟后执行
task_time = utc_ctime + time_delay

# 使用apply_async并设定时间
result = send_email.apply_async(args=["egon"], eta=task_time)
print(result.id)