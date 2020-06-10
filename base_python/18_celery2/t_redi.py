import redis

r = redis.Redis(host='172.16.2.225',port=6379,db=1)


for i in r.lrange('celery',0,-1):
    print(i)