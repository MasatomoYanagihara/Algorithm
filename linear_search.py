data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
flag = False
query = int(input('探したい数字を入力して下さい。'))

for i in range(len(data)):
    if (query == data[i]):
        print(i+1, '番目にあります。')
        flag = True
        break

if flag == False:
    print('見つかりませんでした。')
