if __name__ == '__main__':
    # eg.1 相当于java中的获取方式 scanf
    # message = input("Tell me your name: ")
    # print(message)

    # eg.2 基本的特征调查
    # name = input('tell me your favourite musician: ')
    # print(f'\n{name} is your musician.')

    # eg.3 清晰的界面设置
    # prompt = 'If you can tell me what job do you want to apply,we can help you. '
    # prompt += 'What skills are you familiar with?'
    # hello = input(prompt)
    # hello = int(hello)
    # print(hello > 20)
    # print(f'\nIt seems that {hello} fascinate you.')

    # eg.4 奇偶性的判断使用
    # message = input('请输入一个不为0的整数： ')
    # message = int(message)
    # if(message % 2 != 0):
    #     print('您输入了一个奇数')
    # else:
    #     print('您输入了一个偶数')

    # eg.5 汽车的租赁
    # message = input('Please input a car type that you need  ')
    # print(f'\nYou need {message},right?')

    #eg.6 餐馆定位
    # message = input('Please input the number of seats that you need? ')
    # i = int(message)
    # if(i > 8):
    #     print('Execuse me,we don\'t have a table available right now.')
    # else:
    #     print('Welcome,we have a table available.')

    #eg.7 判断是否是10的整数倍
    # message = input('please input a number. ')
    # i = int(message)
    # if i % 10 == 0:
    #     print("您输入了一个10的倍数")
    # else:
    #     print("您尚且没有输出10的倍数")
    # dictionary = 110
    # while dictionary < 135:
    #     print('take challenge.')
    #     dictionary += 10

    #eg.8 输入检验
    # prompt = "\n Will is everything. "
    # prompt += "\n Action speaks louder than words."
    # prompt += "\n PLease input your desire.\n"
    # message = ""
    # while message != "quit":
    #     message = input(prompt)
    #     if message != 'quit':
    #         print(message)

    #eg.9 flag 标志符检验
    # prompt = '\n core competence'
    # prompt += '\n data etl'
    # prompt += '\n input something you need to practice .'
    # flag =True
    # while flag:
    #     s = input(prompt)
    #     if s =='quit':
    #         print('learn how to find your main task\n')
    #     else:
    #        print('Deliberate practice more\n')

    #eg.10 flag 标志符检验
    # prompt = "Tell me which city do you want to go."
    # prompt += "\n input here."
    # message = ""
    # while True:
    #     message = input(prompt)
    #     if message != "quit":
    #         print(f"You want to go to {message},right?")
    #     elif message == "quit":
    #         print(f"See you")
    #         break;

    #eg.11 循环使用 continue,跳出当前循环
    # current_number = 0
    # while current_number < 10:
    #     current_number += 1
    #     if current_number % 2 == 0:
    #         continue
    #     print(current_number)

   #eg.12 Pizza
   # info = "Please input something you want in the pizza\n"
   # Pizza = []
   # message = ""
   # while True:
   #     message = input(info)
   #     if(message == "quit"):
   #         print("bye")
   #         break
   #     else:
   #         Pizza.append(message)
   #         print(f"You put {message},right?")
   # print(f"In pizza,you put: ")
   # for i in Pizza:
   #      print(f"{i}")

   #eg.12 Tickets
   # info = "To help you better get a reasonable ticket,we need you to input your age.\n"
   # print(info)
   # message =""
   # while True:
   #     s = input(message)
   #     if int(s) in range(1,3):
   #         print('Charge free')
   #         break
   #     elif int(s) in range(3,12):
   #         print('10 $')
   #         break
   #     elif int(s) > 12:
   #         print('15 $')
   #         break

   #eg.13 active  python中的常见浮点型的操作方式
   # printInfo = "What's your age?\n"
   # message1 = ""
   # active = True
   # while active:
   #     message1 = input(printInfo)
   #     if float(message1) in range(0,3):
   #         print(" 0 $")
   #     elif  float(message1) in range(2,13):
   #         print(" 10 $")
   #     elif  float(message1) > 12:
   #         print("15 $")
   #     elif message1 == 'quit':
   #         active =False
   #     else:
   #         print("You input a wrong number,please input again.")

   #eg.14 使用while循环处理列表和字典
   unconfirmed_users = ['Rakesh Agrawal','Jiawei Han','Jon Kleinberg','Qiang Yang','Wei Wang','Zhou Zhihua']
   confirmed_users = []
   while unconfirmed_users:
       current_users = unconfirmed_users.pop()
       print(f"\n verifying users.{current_users}")
       confirmed_users.append(current_users)
   print(confirmed_users)