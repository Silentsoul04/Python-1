class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

       # 1.使用类名创建对象的时候，new方法会被自动调用
       print("Create object and Allocate space")

       # 2. 为对象分配空间
       instance = super().__new__(cls)

       # 3. 返回对象的引用
       return instance

    def __init__(self):

        print("Initialize the musicplayer")

Player = MusicPlayer()

print(Player)