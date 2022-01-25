from car import Car
if __name__ == '__main__':
    #eg.1直接修改
    # car = Car('Tesla', 'Model3', 2022)
    # car.get_descriptive_name()
    # car.read_odometer()

    #eg.2通过方法去修改名称
    #eg编程的过程中，注意查看自己是否有重复的进行编程的情况
    # Motor = Car('Honda', 'Yamaha', 2022)
    # Motor.get_descriptive_name()
    # Motor.update_odometer(23)
    # Motor.read_odometer()

    #eg添加自己的行程增量
    car1 = Car('Honda', 'DreamWing', 2022)
    car1.get_descriptive_name()
    car1.update_odometer(202)
    car1.read_odometer()
    car1.increment_odometer(11)
    car1.read_odometer()

    #eg 继承的实现
    #eg 实现继承的方式
    # electric_car = ElectricCar('Tesla', 'Model S', 2019)
    # electric_car.get_descriptive_name()
    # electric_car.battery.describe_battery()
    # electric_car.battery.get_range()

    #续航里程的增加
    # car = ElectricCar('Honda','Little Rocket',2022)
    # car.get_descriptive_name()
    # car.battery.get_range()
    # car.battery.upgrade_battery()
    # car.battery.get_range()

