# mecab-python3モジュールをインポート
import MeCab

# 形態素解析を行うオブジェクトを生成
m = MeCab.Tagger()

# sample.txtを読み込み，一行ごとに処理
with open("..//data//sample.txt", encoding="utf-8") as f:
    for line in f:
        # 一行を形態素解析し，解析結果を表示
        terms = m.parse(line)
        print(terms)
