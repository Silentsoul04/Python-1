class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self,player_name):
        self.play_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让它进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始啦" % self.play_name)


# 1. 查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分 使用类方法和静态方法之前不用定义对象，通过类名.方法来调用
Game.show_top_score()

# 3.创建游戏形象 对象的实例方法要创建对象后通过对象.来调用
gameplayer1 = Game("jason")
gameplayer1.start_game()