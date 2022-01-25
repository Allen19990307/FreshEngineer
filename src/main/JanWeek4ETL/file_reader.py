# 向数据ETL出发  读取文件方法1.当前目录，使用当前目录及其以下的目录  读取文件方法2.使用绝对路径，双反斜杠
# with open('D:\\Allen‘s repository\\FreshEngineer\\src\\main\\JanWeek4ETL\\Resource\\pi_digits.txt') as file_object:
    #eg.1 原样输出
    # read = file_object.read()
    # print(read.rstrip())

    #eg.2 文件输出的时候，末尾，print()都会有换行符号
    # for line in file_object:
    #     print(line)

    #eg.3 各行存储在一个列表中
    # readlines = file_object.readlines()

with open("Resource/python_learning.txt") as file_object1:
    #eg.1 全部打印
    # read = file_object1.read()
    # print(read)

    #eg.2 逐行打印
    # for i in file_object1:
    #     print(i)

    #eg.3 10-1 Python学习笔记  存储到列表当中
    # l1 = []
    # for i in file_object1:
    #     l1.append(i.strip())
    # print(l1)

    #10-2 C语言的学习笔记
    l1 = ""
    for i in file_object1:
        l1 += i
    replace_object = l1.replace('Python', 'C')
    print(replace_object)
