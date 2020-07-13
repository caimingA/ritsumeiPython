if __name__ == '__main__':
    dic = {'access': 'アクセス', 'retrieval': '検索 ', 'bag': 'かばん', 'example': '例'}
    while True:
        target = input("英単語を入力して下さい:")
        if target in dic:
            print(target, "の日本語訳語は「", dic[target], "」です")
        else:
            print(target, "は辞書に含まれていません")

        if input("進めますか（yes/no）:") == "no":
            break
