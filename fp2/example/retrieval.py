# 文書を表すクラス
class Document:
    # コンストラクタ
    def __init__ (self, doc_id, doc_name, vec_length):
        self.doc_id = doc_id		# 文書ID
        self.doc_name = doc_name	# 文書名
        self.vec_length = vec_length	# 文書ベクトル長
        self.score = 0.0		# 文書のスコア（検索時に計算）

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

inv = {}	# 転置索引を格納する辞書型変数
doc = []	# 文書オブジェクトのリスト
n_docs = 100	# 文書数

# (1)転置索引のファイルinv.txtを読み込み，辞書型変数invに格納
with open("inv.txt", encoding="utf-8") as f:
    for line in f:
        ## ここに処理を記述すること ##

# (2)文書オブジェクトのリストを作成し，初期化
for i in range(n_docs):
    # 仮の文書名（doc_文書ID）で文書オブジェクトを生成し，リストに追加
    doc.append(Document(i, "doc_" + str(i), 0.0))

# (3)ユーザによる検索語の入力
query_str = input("検索語を入力して下さい: ")

# (4)検索語ごとに転置索引を参照し，文書スコアを計算
query_terms = query_str.split()
for term in query_terms:
    ## ここに処理を記述すること ##

# (5)検索結果の出力
for i in range(n_docs):
    # スコアが0.0を超える文書（索引語が含まれる文書）のみ出力
    ## ここに処理を記述すること ##
