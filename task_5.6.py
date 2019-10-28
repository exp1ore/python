d = {}
in_f = open("file_5_6.txt", "r")
while True:
    content = in_f.readline()
    if content != "":
        ll = content.split()
        ll_sum = []
        i = 1
        while i <= len(ll)-1:
            if ll[i].isdigit():
                ll_sum.append(int(ll[i]))
                i = i + 1
            else:
                print("Неверный формат")
                i = i + 1
        _d = dict.fromkeys([ll[0]], sum(ll_sum))
        d.update(_d)
        print(ll)
    else:
        print("Чтение файла завершено")
        break
in_f.close()
print(d)
