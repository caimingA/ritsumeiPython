import MeCab


def read_txt():
    m = MeCab.Tagger()
    f = open("wikisamp.txt", encoding="utf-8")
    result = dict()
    for line in f:
        # print(line)
        terms = m.parse(line)
        # print(terms)
        for i in terms.splitlines():
            temp = i.split('\t')
            # print(temp)
            if temp[0] != 'EOS':
                if temp[0] in result:
                    result[temp[0]] += 1
                else:
                    result[temp[0]] = 1
    f.close()

    f = open("tf2.txt", mode="w", encoding="utf-8")
    for key, value in result.items():
        f.write(key+":"+str(value) + "\n")
        print(key+":"+str(value))

    f.close()


if __name__ == '__main__':
    read_txt()
