class Animal:

    def eat(self):
        print("eat---")

    def drink(self):
        print("drink---")

    def run(self):
        print("run---")

    def sleep(self):
        print("sleep---")


class Dog(Animal):

    def bark(self):
        print("bark,bark,bark")


class XiaoTianQuan(Dog):

    def fly(self):
        print("I believe I can fly")

    def bark(self):
        print("bark as xiaotian")

xtq = XiaoTianQuan()

xtq.bark()