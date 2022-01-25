if __name__ == '__main__':
    # eg.1 if的使用  判断条件的：and 和 or  !=  判断字段是否在其中 in
    # cars = ['nissan','honda','toyota']
    # for i in cars:
    #     if(i == 'nissan'):
    #         print(i.capitalize())
    #     else:
    #         print(i.title())

    # eg.2 not in的条件判断
    # if 'Nissan' not in cars:
    #      print('Allen is keeping fight.')
    # else:
    #      print('I love coding.')

    # eg.3 判断是否相同的条件 ==
    # if 'Nissan' == 'nissan':
    #     print('true')
    # else:
    #     print('I love coding1.')
    # print('practice FLUENTLY'.lower())

    # eg.4 if elif条件的使用范围：只需要一个条件的情况 ，elif作为结束语句的使用，避免恶意参数例如 -6000的加入
    # WorkTime = 2
    # if(WorkTime > 25):
    #     print('您已经超出最长的休息时间，请您保持合理的专注时间')
    # elif(WorkTime >= 20 and WorkTime < 25 ):
    #     print('当下你的专注时间即将结束，请做好工作的结束准备')
    # elif(WorkTime in range(0,25)):
    #     print('你的工作时间刚刚开始，让我们一起全力以赴！')

    # eg.5 判断外星人的血液颜色
    # alien_color = 'yellow'
    # if(alien_color == 'green'):
    #     print('you got 5 points!')
    # else:
    #     print('keep going')
    # alien_color1 = 'green'
    # if(alien_color1 == 'green'):
    #     print('you got 5 points!')
    # else:
    #     print('keep going')

   # eg.6 offer Test
   #  result = 'offer'
   #  if(result == 'offer'):
   #      print('Congratulation!')
   #  else:
   #      print('Enjoy reviewing')
   #  result = 'no offer'
   #  if(result == 'offer'):
   #      print('Congratulation!')
   #  else:
   #      print('Enjoy reviewing')

   # eg.7 Offer Level
   # result = 'ByteDance'
   # if(result == 'Alibaba'):
   #     print('You gotta 5 points.')
   # elif(result == 'Baidu'):
   #     print('You gotta 10 points.')
   # elif(result == 'ByteDance'):
   #     print('Welcome to ByteDance.')

   # eg.8 Life Span
   # life_phase = 52
   # if life_phase in range(10,20):
   #     print("Play hard,Work hard.")
   # elif life_phase in range(20,30):
   #     print("Establish your goal.")
   # elif life_phase in range(30,40):
   #     print("Foucs on your career")
   # elif life_phase in range(40,50):
   #     print("Lead your team to get a better result.")
   # elif life_phase >50:
   #     print("Help young people to find their life goal.")

   # eg.9 Function realize
   # function =['time scheduler','job handler','problem solver']
   # if('time scheduler' in function):
   #     print('You really know how to use time')
   # if('job handler' in function):
   #      print('You really know how to handle job')
   # if('problem solver' in function):
   #      print('You really know how to solve problems')

   # eg.10 Filter something that we want it appear
   # request_material = ['beef','rice','corn','spaghetti']
   # for i in request_material:
   #     if(i == 'spaghetti'):
   #         print(f'we ran out of {i}')
   #     else:
   #         print(f'{i} added.')
   # print('Enjoy your food.')

   # eg.11 Blank confirm
   # request_conditions = ['heart to make products better','the sense of data','the ability to solve problems','skills we learn']
   # if request_conditions:
   #     for i in request_conditions:
   #          print(f'{i} added')
   #     print('Job finished.')
   # else:
   #     print('Are you want to touch fish?')

   #eg.12 Provide and need balance
   # request_conditions = ['beef','rice','corn','spaghetti']
   # provide_conditions = ['beef','rice','potato','milk']
   # for request in request_conditions:
   #     if(request in provide_conditions):
   #         print(f'{request} add.')
   #     else:
   #         print(f'Execuse me,we didn\'t have {request}')
   # print(f'Things are done.')

   #eg.13 Design Course
   # Stanford = ['Evaluate','Compass','Way','Dilemma','Prototype','Offer','Design','Active','Imunity']
   # Stanford = []
   # if Stanford:
   #     for step in Stanford:
   #         if(step == 'Evaluate'):
   #             print(f'Hello,would you like to make a life change? {step} Now')
   #         else:
   #             print(f'Now,you can have a {step}')
   #     print('Life can be designed like what you desire.')
   # else:
   #     print('Just go and enjoy your life!')

  #eg.14 Users 去除重复的部分
   # Current_Users = ['Jimmy','Allen','Blair','Cathy','Dorothy']
   # New_Users =['Ethan','Frank','Gorge','Helen','Allen']
   # Current_Users1 = [i.lower() for i in Current_Users]
   # for newUsers in New_Users:
   #     if newUsers.lower() in Current_Users1:
   #         print(f'{newUsers} has been used.')
   #     else:
   #         print(f'{newUsers} hasn\'t been used.')
   # print('Work is done.')

   #eg.15 Number compare
   # number = [i for i in range(1,10)]
   # for num in number:
   #     if num == 1:
   #         print('1st')
   #     elif num == 2:
   #         print('2nd')
   #     elif num == 3:
   #         print('3rd')
   #     elif num == 4:
   #         print('4th')
   #     elif num == 5:
   #         print('5th')
   #     elif num == 6:
   #         print('6th')
   #     elif num == 7:
   #         print('7th')
   #     elif num == 8:
   #         print('8th')
   #     else:
   #         print('9th')

   #eg.16 Think different
   ideas = ['life pattern design','basic knowlegde','algotithm','sharpen tools']
   print(f'很高兴和你一起升级带怪,在开发的道路上，希望我们能够走得更加稳健')
   for idea in ideas:
       print({idea})