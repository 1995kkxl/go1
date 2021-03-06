from collections.abc import Iterable
from collections.abc import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用for，那么必实现————iter————方法"""
        return self
    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num +=1
            return ret
        else:
            raise StopIteration


classmate = Classmate()


classmate.add("老王")
classmate.add("老王1")
classmate.add("老王2")
classmate.add("老王3")


# print("判断classmate是否可以迭代的对象：",isinstance(classmate,Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate是否可以迭代器：",isinstance(classmate_iterator,Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)