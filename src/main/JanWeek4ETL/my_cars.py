from car import Car as ca,ElectricCar as ec
# 从一个模块下导入多个类
vision = ca('Stellantis', 'Jeep', 2025)
vision.get_descriptive_name()
electric_car = ec('Xiaomi', 'MiCar', 2025)
electric_car.get_descriptive_name()