import time

def set_func(func):
    def call_func(numasd12): #numasd12传入的是形参 可以瞎写名
        print("----权限验证一------")
        print("----权限验证二------")
        func(numasd12)
    return call_func

@set_func
def fitst(num):
    print("最开始的方法---%d" % num)

fitst(100)