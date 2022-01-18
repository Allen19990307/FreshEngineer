# python用来书写脚本的基本语法规则,列表;for循环的使用;注意缩进  TOYOTA、NISSAN、HONDA、LEXUS、INFINITI、SUBARU
if __name__ == '__main__':
    traits = ['long_termism','wills','patience']
    friends = ['Dorothy','Allen','Zero','Cathy']
    transport = ['Honda','Nissan','Toyota']
    traits.append('skills')
    friends.append('Jason')
    transport.append('Lexus')
    for i in range (0,4):
        hello = f"Hello,{friends[i].title()}. "
        allen = f"Allen gives {traits[i].title()}"
        print(hello + allen)
    print("allen_keep_going")
    for motor in transport:
        print(f"I would like to own {motor} motor.")
