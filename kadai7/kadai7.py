import MeCab
import os
import glob
import math


def get_wiki():
    filenames = list()
    files = glob.glob("../fp2/data/wiki/*.txt")
    files.sort()

    for file in files:
        filename = os.path.basename(file)
        filenames.append(filename)

    return filenames


def make_index(files):

    m = MeCab.Tagger()
    g = open("doc_data.txt", mode="w", encoding="utf-8")
    results = dict()
    # inv.txtの作り方と同じ
    for ID, file in enumerate(files):
        f = open('../fp2/data/wiki/' + file, encoding="utf-8")
        # print(ID)
        vecCount = 0

        for line in f:
            terms = m.parse(line)
            # print(line)
            for i in terms.splitlines():
                temp = i.split('\t')
                # print(temp)
                if temp[0] != 'EOS':
                    # print()
                    adj = temp[1].split(',')
                    # print(adj)
                    if adj[0] == '名詞':
                        if temp[0] in results:
                            if ID in results[temp[0]]:
                                results[temp[0]][ID] += 1
                            else:
                                results[temp[0]][ID] = 1
                        else:
                            results[temp[0]] = {ID: 1}

        # 2乗を計算
        for value in results.values():
            if ID in value.keys():
                vecCount += value[ID] ** 2

        # print(vecCount)
        line = str(ID) + "\t" + file.replace('.txt', '') + "\t" + str(math.sqrt(vecCount)) + "\n"
        g.write(line)
        print(line, end="")
        # print(results)
        f.close()

    g.close()


if __name__ == '__main__':
    wiki = get_wiki()
    make_index(wiki)
