#代码创建文件并添加内容
# new_write="内容\n"
# with open('python.txt','a',encoding="UTF-8") as f:
#     f.write(new_write)
#输出内容
# f=open('python.txt','r',encoding="UTF-8")
# content=f.readlines()
# print(content)
# f.close()

#只读取一行内容
# f=open('python.txt','r',encoding="UTF-8")
# content=f.readline()
# print(f'第一行：{content}')
# content=f.readline()
# print(f'第二行：{content}')
f=open("python.txt","r",encoding="UTF-8")
for line in f:
    print(line,end='')

#关闭文件，以免占用内存
f.close()