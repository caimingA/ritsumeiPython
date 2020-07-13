import re
import MeCab
import os
import glob


def get_wiki():
    filenames = list()
    files = glob.glob("new_txt/*.txt")
    files.sort()

    for file in files:
        filename = os.path.basename(file)
        filenames.append(filename)

    return filenames


def read_inv():
    inv = dict()
    keys = dict()
    counter = 0
    f = open('inv.txt', encoding="utf-8")
    for line in f:
        line = line.split("\t")
        temp = line[1].replace('\n', '')
        temp = re.split(',|:', temp)
        tempDict = dict()
        for i in range(0, len(temp), 2):
            tempDict[int(temp[i])] = int(temp[i + 1])
        inv[line[0]] = tempDict
        keys[line[0]] = counter
        counter += 1
    f.close()
    return inv, keys


def read_doc_id_name():
    idAndName = dict()
    f = open('doc_id_name.txt', encoding="utf-8")
    for line in f:
        idAndName[int(line.split('\t')[0])] = line.split('\t')[1].replace('\n', '')

    return idAndName


def renewInv(inv, newTxt, names):
    num = len(names)
    # print(names)
    m = MeCab.Tagger()
    for ID, file in enumerate(newTxt):
        id = ID + num
        f = open('new_txt/' + file, encoding="utf-8")
        g = open('new_doc_id_name.txt', mode='w', encoding='utf-8')
        names[id] = file
        g.write(str(id)+'\t'+file+'\n')
        g.close()
        # print(id)
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
                        if temp[0] in inv:
                            # inv[temp[0]][id] += 1
                            if id in inv[temp[0]]:
                                inv[temp[0]][id] += 1
                            else:
                                inv[temp[0]][id] = 1
                        else:
                            inv[temp[0]] = {id: 1}
        # print(inv)
        f.close()

        # 書き込み
        f = open("new_inv.txt", mode="w", encoding="utf-8")
        for key, value in inv.items():
            # print(key, value)
            line = key + "\t"
            for Id, times in value.items():
                line += str(Id) + ':' + str(times) + ','
            line = line[: -1]
            f.write(line + "\n")
            # print(line)

        f.close()


if __name__ == '__main__':
    newTxt = get_wiki()
    inv, keys = read_inv()
    names = read_doc_id_name()
    renewInv(inv, newTxt, names)
    print('renew finish')
