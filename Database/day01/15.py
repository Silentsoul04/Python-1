class Gun:

    def __init__(self,model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:

            print("[%s] 子弹不够了，快装弹" % self.model)
            return

        # 2.发射子弹，-1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("老子刚刚发射了一枚子弹，可还行")
        print("[%s] 突突突... [%d]" % (self.model,self.bullet_count))


class Soldier:

    def __init__(self,name):

        # 1.姓名
        self.name = name

        # 2.枪 - 新兵没有枪
        self.gun = None


ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()

# 2.创建许三多




