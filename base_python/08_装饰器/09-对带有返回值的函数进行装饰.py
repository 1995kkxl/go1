import time

def set_func(func):
    print("----开始装饰")
    def call_func(*args,**kwargs): #传入的是形参 可以瞎写名
        print("----权限验证一------")
        print("----权限验证二------")
        #func(args,kwargs) #不行 args,kwargs，相当于传递2个参数，1个元组，1个字典
        return func(*args,**kwargs) #拆包
    return call_func

@set_func
def fitst(num,*args,**kwargs):
    print("最开始的方法---%d" % num)
    print("最开始的方法1---" , args)
    print("最开始的方法2---" , kwargs)
    return "ok..." #返回值

@set_func
def second():
    pass


ret = fitst(100)
print(ret)


ret = second(100)
print(ret)