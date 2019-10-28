import json


# Функция вычисления среднего значения
def f_avr(var_1):
    return 0 if not var_1 else sum(var_1)/len(var_1)


ll_pr = []
d = {}
in_f = open("file_5_7.txt", "r")
while True:
    content = in_f.readline()
    if content != "":
        ll = content.split()
        if ll[2].isdigit() and ll[3].isdigit():
            pr = int(ll[2]) - int(ll[3])
            if pr > 0:
                ll_pr.append(pr)
            else:
                print("Убыточная компания:")
        else:
            pr = None
            print("Неверный формат выручки/издержек")
        _d = dict.fromkeys([ll[0]], pr)
        d.update(_d)
        print(ll)
    else:
        print("Чтение файла завершено")
        break
in_f.close()
ll_total = [d, dict.fromkeys(['average profit'], int(f_avr(ll_pr)))]

with open("file_5_7.json", "w") as write_f:
    json.dump(ll_total, write_f)

with open("file_5_7.json") as read_f:
    data = json.load(read_f)
print("Итог чтения json файла", data)
print("Тип данных:", type(data))
