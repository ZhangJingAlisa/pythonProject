import os

# os.rename("test-复制1.txt","不要.txt")
# os.remove("不要.txt")

# os.mkdir("创建文件夹")
# os.rmdir("创建文件夹")

# print(os.getcwd())
# print(os.listdir("./"))

# 批量修改文件名称
curpath = "./创建文件夹/"
items = os.listdir("创建文件夹")
# path = os.getcwd() + "\创建文件夹"
os.chdir(curpath)

# 如果为1，则添加；为2则删除
flag = 2

for item in items:
    index = item.find(".")
    filename = item[:index]
    houzhui = item[index:]
    if flag == 1:
        newFileName = filename + "new" + houzhui

        os.rename(item,newFileName)
    if flag == 2:
        num = len("new")
        newFileName = filename[:-num] + houzhui
        # print(newFileName)
        os.rename(item, newFileName)