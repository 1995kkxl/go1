import re

"""替换结果 并且调用函数+1 然后回去"""


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r'\d+',add,"python = 998") #add会调用函数执行 返回的结果
print(ret)

ret = re.sub(r'\d+',add,"python = 99")
print(ret)
