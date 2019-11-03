d = {"wage": 0, "bonus": 0}


class Worker:
    name = None
    surname = None
    position = None
    _income = d


class Position(Worker):
    def get_full_name(self):
        return print(self.name, self.surname)

    def get_total_income(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        return print(self._income["wage"] + self._income["bonus"])


p = Position()
p.name = "Piter"
p.surname = "Pen"
p.get_full_name()
p.get_total_income(50, 20)

p2 = Position()
p2.name = "Ivan"
p2.surname = "Ivanov"
p2.get_full_name()
p2.get_total_income(100, 90)
