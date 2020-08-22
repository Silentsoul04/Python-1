class Tool(object):

    count = 0

    def __init__(self,name):
        self.name = name

        Tool.count += 1


tool1 = Tool("gun")
tool2 = Tool("stick")
tool3 = Tool("sword")

tool3.count = 99
print("工具对象总数 %d" % tool3.count)
print("===> %d" % Tool.count)