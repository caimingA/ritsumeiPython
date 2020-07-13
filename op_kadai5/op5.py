import re
import numpy as np

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


def boolean_transform(inv, keys, names):
    boolean_list =list()
    n = len(keys)
    m = len(names)
    for key, value in inv.items():
        temp = list()
        for i in range(m):
            if i in value:
                temp.append(1)
            else:
                temp.append(0)
        boolean_list.append(temp)
    return boolean_list


def document_init(names):
    documents = list()
    for i in range(n_docs):
        documents.append(Document(i, names[i], 0.0))

    return documents

def prio(op):
    if op == 'NOT':
        return 3
    elif op == 'AND':
        return 2
    elif op == 'OR':
        return 1
    elif op == '(':
        return 0
    else:
        return -1


def in_to_post(target):
    result = list()
    op_list = list()
    for i in range(len(target)):
        if target[i] == ')':
            flag = 1
            while flag:
                result.append(op_list[len(op_list) - 1])
                op_list.pop()
                if op_list[len(op_list)-1] == '(':
                    op_list.pop()
                    flag = 0

        elif target[i] in ['AND', 'OR', 'NOT', '(']:
            if len(op_list) == 0:
                op_list.append(target[i])
            elif prio(op_list[len(op_list) - 1]) < prio(target[i]):
                op_list.append(target[i])
            else:
                flag = 1
                while flag:
                    result.append(op_list[len(op_list)-1])
                    op_list.pop()
                    if len(op_list) == 0:
                        flag = 0
                    else:
                        if prio(op_list[len(op_list) - 1]) < prio(target[i]):
                            flag = 0
                op_list.append(target[i])

        else:
            result.append(target[i])
        if i == len(target) - 1:
            flag = 1
            while flag:
                result.append(op_list[len(op_list) - 1])
                op_list.pop()
                if len(op_list) == 0:
                    flag = 0
    return result


def boolean_search(targets, keys, booleanMatrix):
    booleanMatrix = np.array(booleanMatrix)
    targets = in_to_post(targets.split(' '))

    stack_word = list()
    for i in targets:
        if i == 'NOT':
            op = stack_word[len(stack_word)-1]
            stack_word.pop()
            stack_word.append(np.logical_not(op))
        elif i == 'AND':
            op1 = stack_word[len(stack_word)-1]
            stack_word.pop()
            op2 = stack_word[len(stack_word) - 1]
            stack_word.pop()
            stack_word.append(np.logical_and(op1, op2))
        elif i == 'OR':
            op1 = stack_word[len(stack_word) - 1]
            stack_word.pop()
            op2 = stack_word[len(stack_word) - 1]
            stack_word.pop()
            stack_word.append(np.logical_or(op1, op2))
        else:
            stack_word.append(booleanMatrix[keys[i]])
    return stack_word[len(stack_word) - 1]


# targets is str
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
    inv, keys = read_inv()
    names = read_doc_id_name()
    # print(inv)
    # print(keys)
    # print(names)
    booleanMatrix = boolean_transform(inv, keys, names)
    # print(booleanMatrix)
    documents = document_init(names)
    # boolean_search("( 草津 OR 京都 ) AND NOT 東京 AND 野球", documents, keys, booleanMatrix)
    targets = input('検索語を入力して下さい(複数の場合半角スペースを分割してください) : ')
    boolean_list = boolean_search(targets, keys, booleanMatrix)
    for i in range(len(boolean_list)):
        if boolean_list[i]:
            # print(i, boolean_list[i])
            print(documents[i].doc_name)
