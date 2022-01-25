if __name__ == '__main__':
    #eg.1 函数模块的使用
    # def greet_user():
    #     print("the courage to be disliked.")
    # greet_user()

    #eg.2 函数,实际参数和形式参数的使用
    # def greet_user(name):
    #     print(f"{name} has the courage to be disliked.")
    # greet_user("Jessca")

    #eg.8-1 message
    # def get_message():
    #     print("This chapter is Function")
    # get_message()

    #eg.8-2 book
    # def favourite_book(name):
    #     print(f"My favourite book is {name}.")
    # favourite_book("Siddhartha")

    #eg.8-3 developer
    # def favourite_animal(type,name):
    #     print(f"{type}'s job:understand {name}'s needs.")
    # favourite_animal("developer","user")

    #eg.8-4 understanding  这边我们也需要观察实际参数的传入值是否匹配
    # def life_type(type,name):
    #   print(f"{type}'s job:understand {name}'s needs.")
    # life_type(type="developer",name="user")
    # life_type("boss","employee")
    # life_type("husband","wife")

    #eg.5 QA Time
    # def fundamental_info():
    #     print("在计算机的学习之路，不要忘记夯实自己的基础，比如关于计算机网络的部分.")
    # fundamental_info()

    #eg.6 形式参数赋予初始值
    # def describe_expertise(math = 'high education',cs = '408'):
    #     print(f"\n{math} ability,")
    #     print(f"{cs} ability.")
    # describe_expertise(math = 'statistics' , cs = 'data science')

    #eg.8-3 T恤，文化衫
    # def make_T_shirt(size,slogan):
    #     print(f"Your T-shirt's size: {size},slogan: {slogan}.")
    # make_T_shirt('XL','IDE is one of my lovers')

    #eg.8-4 大号T恤
    # def make_New_shirt(size,slogan = 'I love Python.'):
    #     print(f"Your T-shirt's size: {size},slogan: {slogan}.")
    # make_New_shirt('XXL')
    # make_New_shirt('XL')
    # make_New_shirt('XL','I am creating a opportunity.')

    #eg.8-5 描绘将要抵达的城市
    # def describe_city(city,country):
    #     print(f"{city} is in {country}")
    # describe_city('Tokyo','Japan')
    # describe_city('Shanghai','China')

    #eg.8-6 前两个城市在加州，最后一个不在加州
    # def describe_city_new(city,country = 'USA' ):
    #     print(f"{city} is in {country}")
    # describe_city_new('Los Angeles')
    # describe_city_new('San Francisco')
    # describe_city_new('Shanghai')

    #eg.8-7 Project_challenge
    def game_developer(name):
        print(f"{name},ready to go.We will develop a alien game where people can control their "
              f"three planes in this game.")
    game_developer('Allen')