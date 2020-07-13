def kadai0_4():

    # path変更が必要
    f = open("E:\\python\kadai\\fp2\\data\\merosu.txt", encoding="utf-8")
    # print(f.read())
    for i, line in enumerate(f):
        if line.find('シラクス') != -1:
            print(i+1, "⾏⽬ : ", line)

    f.close()


if __name__ == '__main__':
    kadai0_4()
