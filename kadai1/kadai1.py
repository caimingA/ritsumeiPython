if __name__ == '__main__':
    f = open("..//fp2//data//morph.txt", encoding="utf-8")
    result = dict()
    for line in f:
        temp = line.split('\t')[0]
        # print(temp)
        if temp in result:
            result[temp] += 1
        else:
            result[temp] = 1

    f.close()

    f = open("tf1.txt", mode="w", encoding="utf-8")
    for key, value in result.items():
        f.write(key+":"+str(value) + "\n")
        print(key+":"+str(value))

    f.close()
