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

    def bark(self):
        print("老子是神犬，当然不一样")
        super().bark()

        # 父类名.方法（self）
        # Dog.bark(self)
        # 注意：如果使用子类调用方法，会出现递归调用 -死循环
        # XiaoTianQuan.bark(self)
        print("我就是，我就是全世界最亮滴仔")


xiaotian = XiaoTianQuan()

xiaotian.bark()
