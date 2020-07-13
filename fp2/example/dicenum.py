# 空の辞書型変数の作成
gengo = {}

# 辞書型変数gengoにキーと値の組を追加
gengo["大正"] = 1912
gengo["昭和"] = 1926
gengo["平成"] = 1989
gengo["令和"] = 2019

# gengoの全てのキーと値を表示
for i in gengo:
    print(i + ": " + str(gengo[i]))
