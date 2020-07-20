class A:

    def test(self):
        print("That's test method")


class B:

    def demo(self):
        print("That's demo method")


class C(A,B):

    pass

c = C()
c.test()
c.demo()