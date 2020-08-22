def demo1():
    result = int(input("请输入一个整数"))
    return result

def demo2():
    return demo1()


try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)