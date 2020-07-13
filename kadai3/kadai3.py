import MeCab
import os
import glob


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
    results = dict()  # データ構造　ー＞　{索引: {文書ID: 頻度}}
    for ID, file in enumerate(files):
        f = open('../fp2/data/wiki/' + file, encoding="utf-8")
        # print(ID)
        for line in f:
            terms = m.parse(line)
            # print(line)
            for i in terms.splitlines():
                temp = i.split('\t')

                if temp[0] != 'EOS':
                    # print()
                    adj = temp[1].split(',')
                    # print(adj)
                    if adj[0] == '名詞':
                        if temp[0] in results:
                            # results[temp[0]][ID] += 1
                            if ID in results[temp[0]]:
                                results[temp[0]][ID] += 1
                            else:
                                results[temp[0]][ID] = 1
                        else:
                            results[temp[0]] = {ID: 1}
        print(results)
        f.close()

        # 書き込み
        f = open("inv.txt", mode="w", encoding="utf-8")
        for key, value in results.items():
            # print(key, value)
            line = key + "\t"
            for Id, times in value.items():
                line += str(Id) + ':' + str(times) + ','
            line = line[: -1]
            f.write(line + "\n")
            # print(line)

        f.close()


if __name__ == '__main__':
    files = get_wiki()
    make_index(files)

