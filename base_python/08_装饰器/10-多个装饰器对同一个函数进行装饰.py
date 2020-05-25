import time

def add_qx(func):
    print("----开始装饰add的功能")
    def call_func(*args,**kwargs): #传入的是形参 可以瞎写名
        print("----add权限一------")
        #func(args,kwargs) #不行 args,kwargs，相当于传递2个参数，1个元组，1个字典
        return func(*args,**kwargs) #拆包
    return call_func

def add_xx(func):
    print("----开始装饰xx的功能")
    def call_func(*args,**kwargs): #传入的是形参 可以瞎写名
        print("----xx权限验证一------")
        #func(args,kwargs) #不行 args,kwargs，相当于传递2个参数，1个元组，1个字典
        return func(*args,**kwargs) #拆包
    return call_func


@add_qx
@add_xx
def fitst(*args,**kwargs):
    print("*-------t1----")

fitst()