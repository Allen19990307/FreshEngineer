if __name__ == '__main__':

    # 4-3.一到100的打印
    # count = []
    # for value in range(1,100):
    #     count.append(value)
    # print(count)


    # value1 = [value for value in range(1,100)]
    # print(value1)

    # 4-4 1-1000000 的内容打印输出
    # value2 = [value for value in range(1,1000000)]
    # for i in value2:
    #     print(i)

    # 4-5 1到1000000的求和操作  注意range的输出范围
    #  value3 = [value for value in range(1,10000001)]
    #  print(sum(value3))

    # 4-6 1-20 之内的奇数完成打印
    # value4  = [value for value in range(1,20,2)]
    # for i in range(0,10):
    #   print(value4[i])

    # 4-7 30及30以内3的倍数，逐个打印
    # value5 = [value for value in range(3,31,3)]
    # for i in value5:
    #     print(i)

    # 4-8 前10个整数的立方打印
    # value6 = [value ** 3 for value in range(1,11)]
    # for i in value6:
    #     print(i)

    #4-9 列表解析前十个整数的立方
    value7 =[value ** 3 for value in range(1,11)]
    print(value7)