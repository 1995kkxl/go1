from collections.abc import Iterable
from collections.abc import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用for，那么必实现————iter————方法"""
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass
    def __next__(self):
        ret = self.obj.names[self.current_num]
        self.current_num +=1
        return ret


classmate = Classmate()


classmate.add("老王")
classmate.add("老王1")
classmate.add("老王2")
classmate.add("老王3")


print("判断classmate是否可以迭代的对象：",isinstance(classmate,Iterable))
classmate_iterator = iter(classmate)
print("判断classmate是否可以迭代器：",isinstance(classmate_iterator,Iterator))
print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)