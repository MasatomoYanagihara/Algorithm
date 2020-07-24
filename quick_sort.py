# データ表示関数
def viewArray(arg):
    out = ''
    for q in arg:
        out += str(q) + ', '
    print(out)

# クイックソート関数
def quicksort(target):
    if len(target) < 1:
        return target
    pivot = target[0]
    smaller = []
    larger = []
    for x in range(1, len(target)):
        if target[x] <= pivot:
            smaller.append(target[x])
        else:
            larger.append(target[x])
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    foo = [pivot]
    return smaller + foo + larger

# main part


data = [56, 85, 96, 6, 22, 10, 94, 71, 38, 43, 63]

print("Before")
viewArray(data)

data = quicksort(data)

print("After")
viewArray(data)
