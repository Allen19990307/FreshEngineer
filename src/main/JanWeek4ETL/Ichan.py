class Ichan:
    def __init__(self,Company_name,Company_type,func):
        """餐馆的名称和年龄"""
        self.Company_name = Company_name
        self.Company_type = Company_type
        self.func = func
    def describe_Company(self):
        if self.Company_type <= 1:
            print(f"{self.Company_name} is {self.Company_type} year old")
        else:
            print(f"{self.Company_name} is {self.Company_type} years old")
    def open_Company(self):
        print("The company is working now.")
class BigdataCompany(Ichan):
    def __init__(self,Company_name,Company_type,func):
        super(BigdataCompany, self).__init__(Company_name,Company_type,func)
        self.func = ['FrontEnd','BackEnd','Leader','Supperter']
    def job_require(self):
        print("这边是我们需要招聘的一些伙伴")
        for i in self.func:
            print(i)