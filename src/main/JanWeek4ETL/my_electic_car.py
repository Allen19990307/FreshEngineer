from car import ElectricCar
car = ElectricCar('Tesla', 'Model 3', 2021)
car.get_descriptive_name()
car.odometer_reading = 18
car.battery.describe_battery()
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()