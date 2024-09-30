class MyInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MyInt({self.value!r})'
    
    def __format__(self, format_spec):
        return format(self.value, format_spec)
    
    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.value + other.value)
        elif isinstance(other, int):
            return MyInt(self.value + other)
        else:
            return NotImplemented
        
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, MyInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented


obj1 = MyInt(1)
# <__main__.MyInt object at 0x10b8517e0>
# This part indicates the object is an instance of the MyInt class, which is define in the __main__ module.
print(obj1)

print(obj1 + 10)
print(10 + obj1)

obj1 += 10
print(obj1)














class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __repr__(self):
        return f'Person(name={self.name!r}, age={self.age!r})'

    def __format__(self, format_spec):
        return format(self.name, format_spec)

person = Person("John", 30)

print("++++++++")

print(str(person))
print(f'{person}')
print(repr(person))