class Car:
    """汽车类的基本属性"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.capacity = 100
    def fill_gas_tank(self):
        print(f"The capacity of this car's gas tank is {self.capacity}L.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading += miles
    def get_descriptive_name(self):
        print(f"{self.make} {self.model} {self.year}")
    def read_odometer(self):
        if self.odometer_reading == 0:
            print(f"This car has {self.odometer_reading} mile on it.")
        else:
            print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    """电动车的实现"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car has no gas tank.")
class Battery:
    """有关汽车电瓶的使用"""
    def __init__(self,battery_size = 75):
        """电瓶参数的初始化设置"""
        self.battery_size = battery_size
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full range.")
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
