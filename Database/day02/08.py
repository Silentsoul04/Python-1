class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private method %d %d" % (self.num1,self.__num2) )

    def  test(self):
        print("public method %d" % self.__num2)
        print(self.__num2)
        self.__test()
class B(A):

    def demo(self):

        # print("访问父类的私有属性 %d" % self.__num2)
        # self.__test()

        print("子类方法 %d" % self.num1)
        self.test()
        pass

b = B()
print(b)
# print(b.num1)
# print(b._num2)
# b.__test()
b.demo()
# print(b.num1)
# b.test()