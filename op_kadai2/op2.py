import re
import math


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
        temp = re.split(',|:', inv[i])
        # print(temp)
        IDF = math.log2(doc_num / (len(temp) / 2))
        for index in range(0, len(temp), 2):
            TF = int(temp[index + 1]) / timeList[index]
            score = documents[int(temp[index])].get_score() + TF * IDF
            documents[int(temp[index])].set_score(score)


if __name__ == '__main__':
    inv = read_inv()
    names = read_doc_id_name()
    # print(inv)
    documents = document_init(names)
    targets = input('検索語を入力して下さい(複数の場合半角スペースを分割してください) : ')
    timeList = count_times(inv)

    result = dict()
    # TF
    print("+++++++++++++++++++++TF+++++++++++++++++++++")
    search_TF(targets, documents, inv, timeList)
    for i in documents:
        if i.get_score() > 0.0:
            # print(i.doc_name, ': ', i.get_score())
            result[i.doc_name] = i.get_score()
    for i in sorted(result.items(), key=lambda item: item[1], reverse=True):
        print(i[0], ":", i[1])

    # reset
    documents_reset(documents)
    # TF-IDF
    print("+++++++++++++++++++TF-IDF+++++++++++++++++++")
    search_TF_IDF(targets, documents, inv, timeList)
    for i in documents:
        if i.get_score() > 0.0:
            # print(i.doc_name, ': ', i.get_score())
            result[i.doc_name] = i.get_score()
    for i in sorted(result.items(), key=lambda item: item[1], reverse=True):
        print(i[0], ":", i[1])
# 京都 草津