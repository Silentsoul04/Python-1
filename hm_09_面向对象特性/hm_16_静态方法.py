class Dog(object):

    @staticmethod
    def run():

        # 不需要访问实例属性也不需要访问类属性的方法
        print("狗狗很帅")

# 通过类名.调用静态方法 -不需要创建对象
Dog.run()