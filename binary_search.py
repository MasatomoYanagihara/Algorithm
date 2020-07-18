b = [1, 6, 10, 12, 21, 22, 25, 29, 38, 43, 44, 63, 71, 85, 94, 96]
flag = 0
nagasa = len(b)
query = int(input('query? '))
start = int(0)
end = int(nagasa-1)
while start <= end:
    center = int((start+end)/2)
    if (query == b[center]):
        flag = 1
        break
    elif query < b[center]:
        end = center-1
    else:
        start = center+1
print('flag=', flag)
