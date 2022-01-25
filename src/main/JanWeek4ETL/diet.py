from random import randint,choices
import random
class Diet:
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        print(f"Now is: ")
        print(randint(1,6))
    def roll_die1(self):
        print("Now is: ")
        print(randint(1,10))
    def roll_die2(self):
        print("Now is: ")
        print(randint(1,20))
class Ticket:
    def __init__(self):
        self.lines = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
        # self.lines = [3,3,'c',2]
        self.lines1 = []
        self.lines2 = ""
    def call(self):
        self.lines1  = random.sample(self.lines,4)
        for j in self.lines1:
            self.lines2 += str(j)
        print(self.lines2)
        print("If you have the 33c2 on your screen,you will win a big prize.")
    def ticketAnalysis(self):
        flag = True
        count = 0
        while flag:
            self.lines1  = random.sample(self.lines,4)
            for j in self.lines1:
                self.lines2 += str(j)
            print(self.lines2+" ")
            print(" ")
            if self.lines2 == '33c2':
                flag = False
                break
            else:
                self.lines2 = ""
            count += 1
        print(f"you execute {count} times.")
if __name__ == '__main__':
    #1.菜单
    # diet = Diet()
    # for i in range(1,11):
    #     diet.roll_die()
    #     diet.roll_die1()
    #     diet.roll_die2()

    #2.彩票
    ticket = Ticket()
    ticket.ticketAnalysis()