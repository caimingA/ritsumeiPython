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
        # inv[line[0]] = line[1].replace('\n', '')
        temp = re.split(':|,', line[1].replace('\n', ''))
        num = dict()
        for i in range(0, len(temp), 2):
            num[temp[i]] = temp[i+1]
        inv[line[0]] = num

    f.close()
    return inv


def read_doc_data():
    idAndNameAndVec = dict()
    f = open('doc_data.txt', encoding="utf-8")
    for line in f:
        temp = line.split('\t')
        idAndNameAndVec[temp[0]] = [temp[1], float(temp[2].replace('\t', ''))]

    return idAndNameAndVec


def document_init(names):
    documents = list()
    for i in range(n_docs):
        documents.append(Document(i, names[str(i)][0], names[str(i)][1]))

    return documents


# targets is str
def search(targets, documents, inv):
    results = dict()
    keys = targets.split(' ')
    length = len(keys)
    for doc in documents:
        dot_product = 0
        ID = str(doc.get_id())
        for i in keys:
            if i in inv:
                tf = 0
                if ID in inv[i]:
                    # print(inv[i])
                    tf = inv[i][ID]
                dot_product += int(tf)
                # print(dot_product)
        cos = dot_product / (doc.get_length() * math.sqrt(length))
        if cos != 0:
            results[doc.get_name()] = cos

    return sorted(results.items(), key=lambda item: item[1], reverse=True)


if __name__ == '__main__':
    inv = read_inv()
    datas = read_doc_data()
    documents = document_init(datas)
    # print(documents[0].vec_length)
    targets = input('検索語を入力して下さい(複数の場合半角スペースを分割してください) : ')
    results = search(targets, documents, inv)

    for i in results:
        print(i[0], ":", i[1])
#草津 京都