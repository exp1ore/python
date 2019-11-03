class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def go(self):
        print("Поехали")

    def stop(self):
        print("Стоп")

    def turn(self, direction):
        print("Поворот на", direction)

    def show_speed(self):
        print("Скорость:", self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости", self.speed)
        else:
            print("Скорость:", self.speed)


class SportCar(Car):

    def get_s_car(self):
        print("Спорт кар")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!", self.speed)
        else:
            print("Скорость:", self.speed)


class PoliceCar(Car):

    def get_p_car(self):
        if self.is_police:
            print("Полицeйская машина")
        else:
            print("Не совсем полицейская машина")


car_1 = TownCar()
car_1.speed = 20
car_1.color = "Blue"
car_1.name = "Smart"
car_1.is_police = False
print("Цвет:", car_1.color)
print("Марка:", car_1.name)
print("Полиция:", car_1.is_police)
car_1.go()
car_1.show_speed()
car_1.turn("лево")

print("Следующая машина")

car_2 = WorkCar()
car_2.speed = 50
car_2.color = "White"
car_2.name = "Ford"
car_2.is_police = False
print("Цвет:", car_2.color)
print("Марка:", car_2.name)
print("Полиция:", car_2.is_police)
car_2.go()
car_2.show_speed()
car_2.turn("право")

print("Следующая машина")

car_3 = SportCar()
car_3.speed = 200
car_3.color = "Red"
car_3.name = "Ferrari"
car_3.is_police = False
print("Цвет:", car_3.color)
print("Марка:", car_3.name)
print("Полиция:", car_3.is_police)
car_3.go()
car_3.show_speed()
car_3.turn("лево")
car_3.get_s_car()

print("Следующая машина")

car_4 = PoliceCar()
car_4.speed = 0
car_4.color = "Blue/White"
car_4.name = "Lada"
car_4.is_police = True
print("Цвет:", car_4.color)
print("Марка", car_4.name)
print("Полиция:", car_4.is_police)
car_4.stop()
car_4.show_speed()
car_4.get_p_car()
