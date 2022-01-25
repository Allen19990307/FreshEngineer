from user import User
class Admin(User):
    def __init__(self,first_name,last_name):
        super(Admin, self).__init__(first_name,last_name)
        privilege = Privilege()
        self.privileges = privilege

class Privilege:
    def show_privileges(self):
        self.privileges = ['Experience share','Career Coach','Motivation']
        print("People can enjoy privileges:")
        for i in self.privileges:
            print(i)