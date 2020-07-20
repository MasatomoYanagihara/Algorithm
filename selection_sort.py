# 表示関数
def viewArray(arg):
    out = ''
    for q in arg:
        out += str(q) + ', '
    print(out)

# 選択ソート関数
def selectionsort(arg):
    for e in range(len(arg)-1, 0, -1):
        for s in range(0, e):
            if arg[s] > arg[e]:
                tmp = arg[s]
                arg[s] = arg[e]
                arg[e] = tmp


data = [56, 85, 96, 6, 22, 10, 94, 71, 38, 43, 63]

# 整列前データ表示
print("Before")
viewArray(data)

# 選択ソート関数実行
selectionsort(data)

# 整列後データ表示
print("After")
viewArray(data)
