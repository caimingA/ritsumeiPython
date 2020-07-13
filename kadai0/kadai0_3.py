def kadai0_3():
    str = "2004/4/1 12:30:59"

    # replaceメソッドは文字列を置換する
    # s = str.replace('/', '年', 1)
    # s = s.replace('/', '月', 1)
    # s = s.replace('/', '日', 1)
    # s = s.replace(':', '時', 1)
    # s = s.replace(':', '分', 1)
    # s = s.replace(':', '秒', 1)
    templist = str.split('/')
    templist2 = templist[2].split(' ')
    templist3 = templist2[1].split(':')
    s = templist[0] + '年' + templist[1] + '月' + templist2[0] + '日 ' + templist3[0] + '時' + templist3[1] + '分' + templist3[2]+ '秒'
    print(s)


if __name__ == '__main__':
    kadai0_3()
