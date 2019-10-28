s = input("Введите цисла через пробел: ")

out_f = open("file_5_5.txt", "w")
out_f.writelines(s)
out_f.close()

in_f = open("file_5_5.txt", "r")
while True:
    content = in_f.readline()
    if content != "":
        ll = content.split()
        sum_ll = []
        i = 0
        while i <= len(ll)-1:
            if ll[i].isdigit():
                ll[i] = int(ll[i])
                sum_ll.append(ll[i])
                i = i + 1
            else:
                print("Некорректный символ")
                i = i + 1
    else:
        print("Чтение файла завершено")
        break
in_f.close()
print(sum(sum_ll))
