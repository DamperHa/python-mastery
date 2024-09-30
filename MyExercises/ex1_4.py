# 封装

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self._age = age
        self.gender = gender

    def get_name(self):
        return self.__name
    
    
obj = Person('张三', 20, '男')
print(obj.get_name())

# 变量被改名了，因此找不到__name属性
print(obj.__name)
print(obj._Person__name)

print(obj._age)

print(obj.gender)