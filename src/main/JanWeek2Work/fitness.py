#操作列表的使用
if __name__ == '__main__':
    #e.g1
    fitnessPro = ['squat','benchpress','deadlift']
    for fit in fitnessPro:
      message = f"I love doing {fit}"
      print(message)
    print("I love keeping fitness. \n")
    #e.g2
    Animal = ['Eagle represents vision','Wolf represents union','Lion represents ambition']
    for zoo in Animal:
        message = f"{zoo},each animal has its own trait."
        print(message)
    print("Show my attitude towards life. \n")
    #e.g3  list数组里的内容  逐个增加or增量增加
    list1 = list(range(1,6))
    list2 = list(range(1,13,2))
    print(list1)
    print(list2)

