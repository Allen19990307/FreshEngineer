from user import User
from rights import Admin
from random import randint,choice
#9-3 User  Vogue
# user = User('Allen', 'Qian')
# user.greet_user()
# user.describe_user()
# user = User('Lisa', 'Chen')
# user.greet_user()
# user.describe_user()

#练习 9-7
admin = Admin('ALLEN','QIAN')
admin.privileges.show_privileges()
players = ['charles','martina','michael','florence','eil','allen','lisa']
print(randint(4,7))
print(choice(players))