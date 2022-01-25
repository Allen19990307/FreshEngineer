#面对对象编程，对抽象的理解。当我们遇见一个比较复杂的过程，我们可以将其分解为关键的步骤
class Dog:
    def __init__(self,name,age):
        """name,age"""
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting. ")
    def roll_over(self):
        print(f"{self.name} rolled over.")


if __name__ == '__main__':
    dog = Dog('Puppy','5')
    dog.sit()
    dog.roll_over()





