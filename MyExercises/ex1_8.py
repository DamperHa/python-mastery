#  i want to classmethod

class MyClass: 
    def __init__(self, value):
        self.value = value

    @classmethod
    def print_value(cls, value):
        print("cls is: ", cls)
        print(value)


class MySubClass(MyClass):
    @classmethod
    def print_value(cls, value):
        print("sub cls is: ", cls)
        print(value)
        super().print_value(value)

MyClass.print_value(10)
MySubClass.print_value(10)


