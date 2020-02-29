class A:

    def test(self):
        print("打印test方法")


class B:

    def demo(self):
        print("打印demo方法")


class C(A,B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


duojicheng = C()
duojicheng.test()
duojicheng.demo()