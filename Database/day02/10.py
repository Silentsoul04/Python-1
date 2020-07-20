class A:

    def test(self):
        print("A ----That's test method")

    def demo(self):
        print("A ----That's demo method")


class B:

    def demo(self):
        print("B ----That's demo method")

    def test(self):
        print("B ----That's test method")


class C(B,A):

    pass

c = C()
c.test()
c.demo()

print(C.__mro__)