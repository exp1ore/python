# Функция вычисления среднего значения
def avr(var_1):
    return 0 if not var_1 else sum(var_1)/len(var_1)


surname = []
salary = []
# Чтение файла
in_f = open("file_5_3.txt", "r")
while True:
    content = in_f.readline()
    if content != "":
        ll = content.split()
        surname.append(ll[0])
        if ll[1].isdigit():
            salary.append(int(ll[1]))
        else:
            print("Неверный формат оклада")
        print(ll)
    else:
        print("Чтение файла завершено")
        break
in_f.close()
# Чтение файла завершено
print(surname, salary)
# Поиск сотрудников с окладом < 20 000 тыс.
i = 0
while i <= len(salary)-1:
    if salary[i] < 20000:
        print("Оклад", surname[i], ":", salary[i])
        i = i + 1
    else:
        i = i + 1
print("Средний оклад = ", int(avr(salary)))
