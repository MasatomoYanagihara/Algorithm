# 表示関数
def viewArray(arg):
    out = ''
    for q in arg:
        out += str(q) + ', '
    print(out)

# バブルソート関数
def bubble_sort(arg):
    for i in range(len(arg)):
        for j in range(len(arg)-1, i, -1):
            if arg[j] < arg[j-1]:
                arg[j], arg[j-1] = arg[j-1], arg[j]


data = [56, 85, 96, 6, 22, 10, 94, 71, 38, 43, 63]

# 整列前データ表示
print("Before")
viewArray(data)

# バブルソート関数実行
bubble_sort(data)

# 整列後データ表示
print("After")
viewArray(data)
