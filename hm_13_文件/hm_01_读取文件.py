# 1. 打开 -- 文件名需要注意大小写
file = open("ReadMe.md",'r',encoding='utf-8')

# 2. 读取
txt = file.read()
print(txt)

# 3. 关闭
file.close()


