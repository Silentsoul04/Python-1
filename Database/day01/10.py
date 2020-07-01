class Person:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight


    def __str__(self):
        return "我的名字是 %s 体重是 %.2f 公斤" % (self.name,self.weight)


    def eat(self):
        self.weight += 1
        print("%s 是吃货，吃完这顿再减肥" % self.name)


    def run(self):
        self.weight -= 0.5
        print("%s 爱跑步，跑步锻炼身体" % self.name)



xiaoming = Person("小明",75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

