# osおよびglobモジュールのインポート
import os
import glob

# ディレクトリ内のすべてのテキストファイルのリストをfilesに格納
files = glob.glob("/kyozai/amaeda/fp2/data/wiki/*.txt")

# リストfilesをファイル名の文字コード順にソート
files.sort()

# リストfilesから一つずつ取り出して処理
for file in files:
    # ファイルのパス部分を取り除き，ファイル名のみを取得
    filename = os.path.basename(file)
    print(filename)
