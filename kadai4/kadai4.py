import re


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


# inv.txtを読み込む
def read_inv():
    inv = dict()
    f = open('inv.txt', encoding="utf-8")
    for line in f:
        line = line.split("\t")
        inv[line[0]] = line[1].replace('\n', '')

    f.close()
    return inv


# クラスdocumentsの初期化
def document_init():
    documents = list()
    for i in range(n_docs):
        documents.append(Document(i, "doc_"+str(i), 0.0))

    return documents


# targets is str
# 捜索メソッド
def search(targets, documents, inv):
    keys = targets.split(' ')
    length = len(keys)
    scale = 1 / length
    for i in keys:
        temp = re.split(',|:', inv[i])
        # print(temp)
        for index in range(0, len(temp), 2):
            documents[int(temp[index])].set_score(documents[int(temp[index])].get_score() + scale)


if __name__ == '__main__':
    inv = read_inv()
    # print(inv)
    documents = document_init()
    targets = input('検索語を入力して下さい(複数の場合半角スペースを分割してください) : ')
    search(targets, documents, inv)
    # outlet
    for i in documents:
        if i.get_score() > 0.0:
            print(i.doc_name, ': ', i.get_score())
