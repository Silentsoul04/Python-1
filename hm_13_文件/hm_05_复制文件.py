# 1.打开
file_read = open("ReadMe.md")
file_write = open("Readme[copy]", "w")


# 2.读-写
text = file_read.read()
file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()