out_f = open("file_5_1.txt", "w")
while True:
    s = input("Введите строку: ")
    if s != "":
        out_f.writelines(s+"\n")
    else:
        print("Конец")
        break
out_f.close()
