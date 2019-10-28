d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
in_f = open("file_5_4_en.txt", "r")
out_f = open("file_5_4_ru.txt", "w")
while True:
    content = in_f.readline()
    if content != "":
        for key in d.keys():
            content = content.replace(key, d[key])
        out_f.writelines(content)
    else:
        print("Чтение файла завершено")
        break
in_f.close()
out_f.close()
