from redis import StrictRedis








if __name__ == '__main__':
    try:
        sr = StrictRedis()
        res = sr.set('name','aaa')
        print (res)
    except Exception as e:
        print (e)