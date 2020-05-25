import time

def set_func(func):
    def call_func():
        print("----权限验证一------")
        print("----权限验证二------")
        func()
    return call_func

@set_func
def fitst():
    print("最开始的方法")

fitst()