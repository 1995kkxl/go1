'''加上h1标签'''


class t11(object):
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("这是装饰器添加的功能....")
        return self.func()
@t11
def get_str():
    return "hhaa"

print(get_str())