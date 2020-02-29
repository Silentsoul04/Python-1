class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

class Dog(Animal):

    def bark(self):
        print("汪汪汪")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

class Cat(Animal):

    def catch(self):
        print("我会抓老鼠")



xiaotian = XiaoTianQuan()

xiaotian.fly()
xiaotian.bark()
xiaotian.sleep()
xiaotian.catch()