list = [ "A5", "D4", "C3", "E2", "B1" ]

sorted_list = sorted(list, key=lambda s: s[1])
print(sorted_list)

list.sort(key=lambda s: s[0], reverse=True)
print(list)
