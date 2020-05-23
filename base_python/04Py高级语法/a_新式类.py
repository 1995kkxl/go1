#私有属性 property

# class Persion(object):
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,value):
#         self.__age = value
#
#     age = property(get_age,set_age)
#
#
# p = Persion()
# print(p.age)
#
# p.age =20
# print(p.age)


#第二种
class Persion(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

p = Persion()
print(p.age)

p.age =20
print(p.age)
