# 1. 打开 -- 文件名需要注意大小写
file = open("ReadMe.md",'r',encoding='utf-8')

# 2. 读取
txt = file.read()
print(txt)
print(len(txt))

print("-" * 50)

text = file.read()
print(text)
print(len(text))

# 3. 关闭
file.close()


