class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private method")

class B(A):

    def demo(self):

        # print("访问父类的私有属性 %d" % self.__num2)
        # self.__test()
        pass

b = B()
print(b)
print(b.num1)
# print(b._num2)
# b.__test()
b.demo()