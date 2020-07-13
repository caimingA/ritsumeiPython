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
    keys = list()
    f = open('inv.txt', encoding="utf-8")
    for line in f:
        line = line.split("\t")
        # inv[line[0]] = line[1].replace('\n', '')
        temp = re.split(':|,', line[1].replace('\n', ''))
        num = dict()
        for i in range(0, len(temp), 2):
            num[temp[i]] = temp[i+1]
        inv[line[0]] = num
        keys.append(line[0])

    f.close()
    return inv, keys


def read_doc_data():
    idAndNameAndVec = dict()
    f = open('doc_data.txt', encoding="utf-8")
    for line in f:
        temp = line.split('\t')
        idAndNameAndVec[temp[0]] = [temp[1], float(temp[2].replace('\t', ''))]

    return sorted(idAndNameAndVec.items(), key=lambda item: item[1][0])
    # return idAndNameAndVec


def document_init(names):
    documents = list()
    for i in range(n_docs):
        documents.append(Document(names[i][0], names[i][1][0], names[i][1][1]))
        # documents.append(Document(i, names[str(i)][0], names[str(i)][1]))
    return documents


def compute_cos(documents, inv, keys):
    doc_num = len(documents)
    cos_matrix = [[0 for i in range(doc_num)] for j in range(doc_num)]
    for i in range(doc_num):
        cos_matrix[i][i] = 1.0
        for j in range(i + 1, doc_num):
            dotProduct = 0
            IDa = str(documents[i].get_id())
            IDb = str(documents[j].get_id())
            # print(IDa)
            for key in keys:
                tf_a = 0
                tf_b = 0
                if IDa in inv[key]:
                    tf_a = int(inv[key][IDa])
                if IDb in inv[key]:
                    tf_b = int(inv[key][IDb])
                dotProduct += tf_a * tf_b
            cos = dotProduct / (documents[i].get_length() * documents[j].get_length())
            cos_matrix[i][j] = cos_matrix[j][i] = cos
    return cos_matrix


if __name__ == '__main__':
    inv, keys = read_inv()
    datas = read_doc_data()
    documents = document_init(datas)
    # print(documents[0].vec_length)
    cos = compute_cos(documents, inv, keys)
    # print(cos)

    length = len(documents)
    f = open('doc_sim.txt', mode='w', encoding='utf-8')
    for i in range(length):
        if i == length - 1:
            f.write(documents[i].get_name() + '\n')
        else:
            f.write(documents[i].get_name() + ',')

    for i in cos:
        f.write(str(i).replace('[', '').replace(']', '') + '\n')
    f.close()
    print("writing finished")
