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

xtq = XiaoTianQuan()
xtq.run()
xtq.bark()
xtq.fly()

