# 必須課題9で作成した人物間のコサイン類似度のデータを読み込み
matrix = []
with open("doc_sim.txt", encoding="utf-8") as f:
    names = f.readline().strip().split(",")
    for line in f:
        data = []
        values = line.strip().split(",")
        for value in values:
            data.append(float(value))
        matrix.append(data)

# 行列の各行の番号（row）とその行の値のリスト（values）を取得
for row, values in enumerate(matrix):
    # 各列の番号（col）と現在の行（row）・列（col）の要素の値を取得
    for col, value in enumerate(values):
        # 行（row），列（col），要素の値（value）を表示
        print("row:" + str(row) + ", col:" + str(col) + ", value:" + str(value))
