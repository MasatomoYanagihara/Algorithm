# 表示関数
def viewArray(arg):
    out = ''
    for q in arg:
        out += str(q) + ', '
    print(out)

# 選択ソート関数（昇順）
def insertion_sort(arg):
    for j in range(1, len(arg)):
        key = arg[j]
        i = j-1
        while i >= 0 and arg[i] > key:
            arg[i+1] = arg[i]
            i = i-1
        arg[i+1] = key


data = [56, 85, 96, 6, 22, 10, 94, 71, 43, 38]  # 要素が10

# 整列前データ表示
print("Before")
viewArray(data)

# 選択ソート関数実行
insertion_sort(data)

# 整列後データ表示
print("After")
viewArray(data)
