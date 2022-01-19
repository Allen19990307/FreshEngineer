if __name__ == '__main__':
    # 列表list可以更改，元组 tuple不可修改
    #  s1 = (1,2)
    #  for i in s1:
    #     print(i)

    # 商业模式 使用切片减少使用的量
    s1 = ('Membership','product','online Content','auction')
    for i in s1:
        print(i)
    s2 = s1[:2]
    for i in s2:
        print(i)
