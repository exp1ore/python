class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")


d_1 = Pen()
d_1.draw()

d_2 = Pencil()
d_2.draw()

d_3 = Handle()
d_3.draw()
