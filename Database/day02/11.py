class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
        print("%s Just play simple game" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s Play in the air" % self.name)

class Person(object):

    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):

        print("%s with %s happy play" % (self.name,dog.name))

        dog.game()

wangcai = Dog("wangcai")
xiaoming = Person("xiaoming")
xiaoming.game_with_dog(wangcai)


