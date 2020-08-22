def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码")
    # 2. 如果用户输入长度 >= 8，返回输入密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果用户输入长度 < 8 ,抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象 -- 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")

    # 2> 主动抛出异常
    raise ex


try:
# 提示用户输入密码
    print(input_password())

except Exception as result:
    print(result)