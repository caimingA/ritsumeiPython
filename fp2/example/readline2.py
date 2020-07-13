f = open("sample.txt", encoding="utf-8")
for line in f:
    print(line, end="")
f.close()
