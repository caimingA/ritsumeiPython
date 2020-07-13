import re
import math
import MeCab
import os
import glob


n_docs = 100


# 文書を表すクラス
class Document:
    # コンストラクタ
    def __init__(self, doc_id, doc_name, vec_length):
        self.doc_id = doc_id            # 文書ID
        self.doc_name = doc_name        # 文書名
        self.vec_length = vec_length    # 文書ベクトル長
        self.score = 0.0                # 文書のスコア（検索時に計算）

    # 文書IDを返すメソッド
    def get_id(self):
        return self.doc_id

    # 文書名を返すメソッド
    def get_name(self):
        return self.doc_name

    # 文書ベクトル長を返すメソッド
    def get_length(self):
        return self.vec_length

    # 文書のスコアを返すメソッド
    def get_score(self):
        return self.score

    # 文書のスコアを設定するメソッド
    def set_score(self, score):
        self.score = score


def read_inv():
    inv = dict()
    f = open('inv.txt', encoding="utf-8")
    for line in f:
        line = line.split("\t")
        inv[line[0]] = line[1].replace('\n', '')

    f.close()
    return inv


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
    resultsLoc = dict()  # データ構造　ー＞　{索引: {文書ID: [位置]]}}
    for ID, file in enumerate(files):
        f = open('../fp2/data/wiki/' + file, encoding="utf-8")
        # print(ID)
        countLoc = 0
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
                        if temp[0] in results:  # 之前有这个索引了
                            # results[temp[0]][ID] += 1
                            if ID in results[temp[0]]:  # 该索引出现在这个文本中过
                                results[temp[0]][ID] += 1
                                resultsLoc[temp[0]][ID].append(countLoc)
                            else:                       # 该索引第一次出现在这个文本中
                                results[temp[0]][ID] = 1
                                resultsLoc[temp[0]][ID] = countLoc
                        else:
                            results[temp[0]] = {ID: 1}  # 这个索引第一次出现
                            resultsLoc[temp[0]] = {ID: [countLoc]}
                        countLoc += 1
        # print(results)
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



def read_doc_id_name():
    idAndName = dict()
    f = open('doc_id_name.txt', encoding="utf-8")
    for line in f:
        idAndName[line.split('\t')[0]] = line.split('\t')[1].replace('\n', '')

    return idAndName


def document_init(names):
    documents = list()
    for i in range(n_docs):
        documents.append(Document(i, names[str(i)], 0.0))

    return documents


def documents_reset(documnets):
    for i in documents:
        i.set_score(0)


def count_times(inv):
    timeList = [0 for i in range(100)]
    # print(inv)
    for key, value in inv.items():
        temp = re.split(',|:', value)
        for i in range(0, len(temp), 2):
            timeList[int(temp[i])] += int(temp[i + 1])

    return timeList


def search_TF(targets, documents, inv, timeList):
    keys = targets.split(' ')
    for i in keys:
        temp = re.split(',|:', inv[i])
        # print(temp)
        for index in range(0, len(temp), 2):
            TF = int(temp[index + 1]) / timeList[index]
            score = documents[int(temp[index])].get_score() + TF
            documents[int(temp[index])].set_score(score)


def search_TF_IDF(targets, documents, inv, timeList):
    doc_num = len(documents)
    keys = targets.split(' ')
    for i in keys:
        if i not in inv:
            print(i, ": no result")
        else:
            temp = re.split(',|:', inv[i])
            # print(temp)
            IDF = math.log2(doc_num / (len(temp) / 2))
            for index in range(0, len(temp), 2):
                TF = int(temp[index + 1]) / timeList[index]
                score = documents[int(temp[index])].get_score() + TF * IDF
                documents[int(temp[index])].set_score(score)


def get_snippet(documnetName):
    f = open('../fp2/data/wiki/' + documnetName + ".txt", encoding="utf-8")
    tempList = list()
    for line in f:
        # print(line.replace("\n", ""))
        # tempList.append(line.replace("\n", ""))
        temp = line.replace("\n", "").split('。')
        for item in temp:
            tempList.append(item)
            print(item, '。')
            if len(tempList) == 3:
                return


if __name__ == '__main__':
    make_index()

    # inv = read_inv()
    # names = read_doc_id_name()
    # # print(inv)
    # documents = document_init(names)
    # targets = input('検索語を入力して下さい(複数の場合半角スペースを分割してください) : ')
    # timeList = count_times(inv)
    #
    # result = dict()
    # # TF-IDF
    # print("+++++++++++++++++++TF-IDF+++++++++++++++++++")
    # search_TF_IDF(targets, documents, inv, timeList)
    # for i in documents:
    #     if i.get_score() > 0.0:
    #         # print(i.doc_name, ': ', i.get_score())
    #         result[i.doc_name] = i.get_score()
    # for i in sorted(result.items(), key=lambda item: item[1], reverse=True):
    #     print(i[0], ":", i[1])
    #     get_snippet(i[0])
    #     print("----------------------------------------")
# 京都 草津
# 東京 都