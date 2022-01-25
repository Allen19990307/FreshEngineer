if __name__ == '__main__':
    # eg.1 字典的使用情况
    # grow_0 = {'Nowsday':'growth','phase':1}
    # attention = grow_0['Nowsday']
    # input('tell me what you want to get in the early phase?')
    # print(f'In the first phase,I will focus on my daily {attention}. ')
    # input('If you are confused with how to measure daily growth? please input 1')
    # print('how much responsibility I shoulder & how many problems I solve.')
    # grow_0['x_expertise'] = 1
    # grow_0['x_position']  = 1
    # print(grow_0)

    # eg.2 进化的速度,注意细节
    # iterate_0 ={'cs basic knowledge':1}
    # iterate_0['cs basic knowledge'] = 2
    # print(f"your current phase is {iterate_0['cs basic knowledge']}")

    # eg.3 判断当前的前进位置，形成增量
    # grow_0 = {'x_expertise':1,'x_position':1,'speed':'medium'}
    # if grow_0['speed'] == 'medium':
    #     x_increment = 2
    # elif grow_0['speed'] == 'inferior':
    #     x_increment = 1
    # elif grow_0['speed'] == 'high':
    #     x_increment = 3
    # grow_0['x_expertise'] = grow_0['x_expertise'] + x_increment
    # print(f"Now you speed can be {grow_0['x_expertise']}.")

    # eg.4 删除键值对
    # grow_0 = {'x_expertise':1,'x_position':1,'speed':'medium'}
    # del grow_0['x_position']
    # print(grow_0)

    # eg.5 熟练使用的代码语言
    # language = {'Allen':'python','Blair':'C','Dorothy':'C++','Ethan':'JAVA'}
    # print(f"Allen's favourite laguage are {language['Allen']} and JAVA.")

    # eg.6 get()方法的使用方式
    # database = {'ods':'metadata','dw':'middle'}
    # get = database.get('ads', '暂时没ads层')
    # print(get)

    # eg.7 dictionary
    #  Simon = {'first_name':'dong','last_name':'tao','age':'18','city':'shanghai'}
    #  print(Simon)

    # eg.8 lucky number
     # LuckyNumber = {'allen':'7','blair':'8'}
     # print(LuckyNumber)
     # terms = {'Slice':'it helps us copy what we need','List':'where we can put our data'}
     # print(f"Slice \n  {terms['Slice']} ")
     # print(f"List \n  {terms['List']} ")

    #eg.9 userRecord
    # user = {'fronEnd':'Understand','backend':'Understand'}
    # for key,value in user.items():
    #     print(f"\n key: {key}")
    #     print(f"\nvalue: {value}")

    # eg.10 ProblemSolve
    # hadoop = {'hdfs':'store','zookeeper':'rule','Hbase':'keyValueStore'}
    # for k,v in hadoop.items():
    #    print(f"{k} function: {v}.")

    # eg.11 遍历所有的键
    # favourite_0 ={
    #   'scenery':'WukangRoad',
    #   'book':'The courage to be disliked',
    #   'film':'The shawshank redemption',
    #   'music':'Mayoyo',
    #   'food':'fitnessFood',
    #   'person':'Haotian'
    # }
    # for love in favourite_0.keys():
    #     print(f"{love}: ?, Allen love")

    #eg.12 lucky number
    # favourite_1 = {
    #     'Yuki':'5368',
    #     'Shiree':'Unknown',
    #     'Dorothy':'111',
    #     'Chuchu':'68',
    #     'Allen':'77'
    #     }
    # friends = ['Allen','Dorothy']
    # for name in favourite_1.keys():
    #     print(f"\n Hi,{name}")
    #
    #     if name in friends:
    #         lucky_number = favourite_1[name].title()
    #         print(f"\n Aha~ {name}, your lucky numeber is {lucky_number}")

    #eg.13 lucky number key值进行遍历
    # favourite_1 = {
    #     'Yuki':'5368',
    #     'Shiree':'Unknown',
    #     'Dorothy':'111',
    #     'Chuchu':'68',
    #     'Allen':'77'
    #     }
    # if 'Haotian' not in favourite_1.keys():
    #     print('take her here,grow together.')

    #eg.14 遍历value的值
    # favourite_1 = {
    #     'Yuki':'5368',
    #     'Shiree':'Unknown',
    #     'Dorothy':'111',
    #     'Chuchu':'68',
    #     'Allen':'77'
    #     }
    # for name in sorted(favourite_1.keys()):
    #     print(f"{name.title()},thank you for coming here.")
    # print("here are some numbers mentioned.")
    # for number in set(favourite_1.values()):
    #     print(number)

    #eg.15 区分集合和字典,前者是元素的集合，后者是key value键值对的形式
    # favourite_drink ={'coffee','tea','milk','water','bubble tea','lemon tea'}
    # print(favourite_1)
    # print(favourite_drink)

    #eg.16 关键术语的字典存储
    # iterms ={
    #  'range':'If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.',
    #  'for':'Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. ',
    #  'break':'Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:',
    #  'pass':'The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:',
    #  'match':'A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it can also extract components (sequence elements or object attributes) from the value into variables.'
    # }
    # for k,v in iterms.items():
    #     print(f"{k} mean: {v}")

    #eg.17 字典功能的查询实现
    # rivers ={'Nile':'Egypt','Amazon River':'Brazil','Yangtze':'China'}
    # for k,v in rivers.items():
    #     print(f"{k} runs through {v}")
    # Important_Figure = ['Lisa','Dad','Mom','Yuki','Shiree','Dorothy','Chuchu','Allen']
    # for i in Important_Figure:
    #     if i in favourite_1.keys():
    #         print(f"\n{i},Thank you for join us.")
    # for j in Important_Figure:
    #         if j not in favourite_1.keys():
    #             print(f"\n{j} I will take you here")

    #eg.18 Friends的字典列表
    # friends_0 = {'Kang':'Finance','age':'33'}
    # friends_1 = {'Qian':'BigData','age':'23'}
    # friends_2 = {'Lin':'Manager','age':'33'}
    # sum = [friends_0,friends_1,friends_2]
    # for i in sum:
    #     print(i)
    # Articles =[]
    # for i in range(1,10):
    #     new_Article ={'Expertise':'CS','Area':'Data process'}
    #     Articles.append(new_Article)
    # print(Articles)

    #eg.19 使用Slice技术，进行格式的修改
    # Articles =[]
    # for pa in Articles[3:8]:
    #     if pa['Expertise'] == 'CS':
    #         pa['phase'] = 'Entreprise'
    #         pa['state'] = 'Enjoy'
    # for i in Articles:
    #     print(i)

    # eg.20 字典的结构,更改相应的数据内容
    # Articles =[]
    # for i in range(1,5):
    #     new_Article ={'Life':'Taker','Method':'Money'}
    #     Articles.append(new_Article)
    # for i in range(5,10):
    #     new_Article ={'Life':'Shower','Method':'Fame'}
    #     Articles.append(new_Article)
    # print(Articles)
    # for i in Articles[3:5]:
    #     if i['Method'] =='Money':
    #         i['Life'] = 'Developer'
    #         i['Method'] = 'Principle'
    #         i['State'] = 'Enjoy'
    # for i in Articles[5:8]:
    #     if i['Method'] =='Fame':
    #         i['Life'] = 'D'
    #         i['Method'] = 'Principle'
    #         i['State'] = 'Enjoy'
    # print(Articles)

    #eg.21 字典中存储列表
    # food ={
    #    'food_type':'fitness',
    #    'material':['chicken','rice']
    # }
    # print(f"you ordered {food['food_type']} food,\nit contains: ")
    # for i in food['material']:
    #     print(i)

    #eg.22 字典里存储每个人擅长的编程语言，体会一下python的语言处理的简洁程度
    # language = {
    #     'Allen':['JAVA','PYTHON','SCALA'],
    #     'Simon':['SHELL'],
    #     'Wang':['Scala'],
    # }
    # 这边的len() 方法的统计，注意是对列表的元素个数进行统计，还是对单个元素长度进行统计
    # for k,v in language.items():
    #     print(f"{k} is good at: ")
    #     if len(v) > 1:
    #         for i in v:
    #                 print(i)
    #     else:
    #         for i in v:
    #          print(f"{k}'s favourite language is {i}")

    #eg.23 python的数据字典具有类json的性质,返回的时候注意string的类型格式
    # users = {
    #     'Wills':{
    #       'Tendency':'9',
    #       'Expertise':'10',
    #       'Consistency':'9'
    #     },
    #     'RightNow':{
    #       'Tendency':'8',
    #       'Expertise':'9.4',
    #       'Consistency':'8'
    #     }
    #   }
    # for k,v in users.items():
    #     print(f'Here is fitness club {k}')
    #     word_of_mouth = f"tendency {v['Tendency']},expertise {v['Expertise']}"
    #     print(word_of_mouth)

    # eg 6-7 People
    #  people = {
    #    'Allen':{'city':'Shanghai','Meetdate':'2022-09-03'},
    #    'Lisa':{'city':'Shanghai','Meetdate':'2022-09-03'},
    #    'Robin':{'city':'Wuhan','Weddingdate':'2032-09-03'}
    #  }
    #  for k,v in people.items():
    #     print(f"\n{k} will meet")
    #     for i,j in v.items():
    #        print(f"{i} & {j}")

    # eg 6-8 Pet
    #  pet = {
    #    'Husky':{'master':'Allen','age':'3','skills':'catch plates'},
    #    'Border Shepherd':{'master':'Lisa','age':'2','skills':'catch newspaper'},
    #    'Labreador':{'master':'Allen','age':'3','skills':'run'}
    #  }
    #  for k,v in pet.items():
    #      print(f"{k}, his basic info.")
    #      for i,j in v.items():
    #          print(f"{i} & {j}")

    #eg 6-9 Places
    # Places = {
    #   'Allen':{'Japan':'Tokyo','USA':'California','Greek':'Athens'}
    # }
    # for k,v in Places.items():
    #     print(f"{k} will go to ")
    #     for i in v.items():
    #         print(f"{i}")

    #eg 6-11 Cities
    # Cities = {
    #   'Tokyo':{'Nation':'Japan','Population':'3kw','Industry':'Bigdata'},
    #   'Shanghai':{'Nation':'China','Population':'3kw','Industry':'Bigdata'},
    #   'Delhi':{'Nation':'India','Population':'3kw','Industry':'Bigdata'}
    # }
    # for k,v in Cities.items():
    #     print(f"{k} details show ")
    #     for i,j in v.items():
    #         print(f"{i},{j}")

    Conclusion = {'list','dictionnary','practice'}
    print(f"Conclusion,{Conclusion}")