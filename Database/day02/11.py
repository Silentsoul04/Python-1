class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
        print("play like a normal dog")

class XiaoTianDog(Dog):

    def game(self):
        print("play at the sky")

class Person(object):

    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print("%s and %s play so happy" % (self.name,dog.name))
        dog.game()

# wangcai = Dog("wangcaicai")
wangcai = XiaoTianDog("wangcai")
xiaoming = Person("xiaomingming")
xiaoming.game_with_dog(wangcai)