# 定义一个简单的对象，包含属性以及方法
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

if __name__ == "__main__":
    s = Stock('GOOG', 100, 490.10)
    print(s.name)
    print(s.shares)
    print(s.price)

    print(s.cost())
    