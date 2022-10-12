fileName = "创建文件夹/test.txt"
oldFile = open(fileName,"rb")

read = oldFile.read()
print(read)

oldFileIndex = fileName.find(".")
oldFileHou = fileName[oldFileIndex:]
oldFileName = fileName[:oldFileIndex]
print(oldFileName)

newFilename = oldFileName + "-复制1" + oldFileHou
print(newFilename)
# 此处是复制文件，因为写入时，没有则会创建一个文件

# 复制图片要用二进制格式，二进制需要在后面添加b字母即可
newFile = open(newFilename,"wb")
newFile.write(read)

oldFile.close()
newFile.close()