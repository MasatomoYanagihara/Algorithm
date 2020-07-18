b = [85, 96, 6, 22, 10, 94, 71, 38, 43, 63]
flag = 0
nagasa = len(b)
query = int(input('query? '))

for i in range(nagasa):
    print('b[{0}]={1} is {2}?'.format(i, b[i], query))
    if (query == b[i]):
        flag = 1
print('flag=', flag)
