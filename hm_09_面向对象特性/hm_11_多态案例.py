class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 是一条普通的小狗" % self.name)

class XiaoTianDog(Dog):
    def game(self):
        print("%s 是可以飞到天上去的大狗" % self.name)

class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 和 %s 快乐的玩耍...." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


wangcai = Dog("旺财")
wangcai.game()

xiaotian = XiaoTianDog("啸天")
xiaotian.game()

xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)