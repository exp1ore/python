in_f = open("file_5_2.txt", "r")
c_str = 0
while True:
    content = in_f.readline()
    if content != "":
        c_str = c_str + 1
        c_words = len(content.split())
        print(c_str, c_words, content.split())
    else:
        print("Конец")
        break
in_f.close()
