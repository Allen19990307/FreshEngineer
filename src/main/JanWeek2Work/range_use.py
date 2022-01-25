if __name__ == '__main__':
    # 使用遍历的技巧,使用乘方的计算
    squares = []
    # 1.最原始的书写，方便掌握规则
    # for value in range (1,11):
    #     values = value ** 2
    #     squares.append(values)
    # print(squares)
    # 2.减少使用多余的变量
    # for value in range (1,11):
    #     squares.append(value ** 2)
    # print(squares)
    # 3.使用列表法进行操作更加简洁
    squares = [value ** 2 for value in range(1,11)]
    print(squares)

