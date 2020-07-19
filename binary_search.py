data = [1, 6, 10, 12, 21, 22, 25, 29, 38, 43, 44, 63, 71, 85, 94]  # dataはソートされている必要がある

flag = 0
query = int(input('探したい数字を入力して下さい。 '))
head = int(0)  # 先頭の添字を代入
tail = int(len(data)-1)  # 末尾の添字を代入

while head <= tail:
    center = int((head+tail)/2)
    if (query == data[center]):
        flag = 1
        break
    elif query < data[center]:
        tail = center-1
    else:
        head = center+1

if flag == 1:
    print(query, 'がありました。')
else:
    print(query, 'はありませんでした。')
