# __slots__
# 限制类的属性 
class Person: 
    # 限制类的属性,一个类最多这些属性
    __slots__ = ['name', 'age', 'gender']

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Person('张三', 20)

print(obj.name)
print(obj.age)
# print(obj.gender)

# 不能添加新的属性
# obj.gender = '男'



# 继承
class Student(Person):
    __slots__ = ['score']

    def __init__(self, name, age, gender, score):
        super().__init__(name, age)
        self.score = score
        self.gender = gender

obj = Student('张三', 20, '男', 100)

print(obj.score)
print(obj.gender)
