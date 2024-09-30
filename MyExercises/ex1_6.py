# 装饰器，setter，getter

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('getter')
        return self.__name
    
    @name.setter
    def name(self, name):
        print('setter')
        self.__name = name



obj = Person('张三', 20)

# 当访问一个变量时，我们喜欢执行一些其他操作，比如打印一些日志，或者在访问之前做一些检查
# 可使用@property装饰器
print(obj.name)

# 当访问一个变量时，我们喜欢执行一些其他操作，比如打印一些日志，或者在访问之前做一些检查
obj.name = '李四'
print(obj.name)
    