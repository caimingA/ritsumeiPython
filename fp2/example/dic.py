# 第1引数に指定したキーが第2引数に指定した辞書型変数に存在するかどうかを
# 判定し表示する関数
def check_key(key, dic):
    if (key in dic):
        print("キー「" + key + "」は存在します．")
    else:
        print("キー「" + key + "」は存在しません．")

# 空の辞書型変数の作成
gengo = {}

# 辞書型変数gengoにキーと値の組を追加
gengo["大正"] = 1912
gengo["昭和"] = 1926
gengo["平成"] = 1989

# gengoに含まれるデータ（キーと値の組）をすべて表示
print(gengo)

# gengoにキー「令和」が含まれるかどうかを判定
check_key("令和", gengo)

# gengoにキーと値の組を追加
gengo["令和"] = 2019

# gengoに含まれるデータ（キーと値の組）をすべて表示
print(gengo)

# gengoにキー「令和」が含まれるかどうかを判定
check_key("令和", gengo)
