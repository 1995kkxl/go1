
class Feibonacci(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1


    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用for，那么必实现————iter————方法"""
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a,self.b = self.b,self.a + self.b
            self.current_num +=1
            return ret
        else:
            raise StopIteration

feibo = Feibonacci(10)

for num in feibo:
    print(num)