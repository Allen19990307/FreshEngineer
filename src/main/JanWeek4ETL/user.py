class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is working hard.")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name},Welcome to our city.")

