# エラトステネスのふるい（素数を求めるアルゴリズム）
# リストの添字を数として、要素が１か０で素数を分ける。

# 平方根を求める為、mathをimportする。
import math

serch_number = int(input('素数を探したい数を入力してください。'))

# リストを生成し全ての要素に１を代入。要素数をプラス１することで、数を合わせる。
data = []
for i in range(serch_number + 1):
    data.append(1)

# エラトステネスのふるい（メイン部分）
sqrt_number = int(math.sqrt(serch_number))
for k in range(sqrt_number):
    if k >= 2 and data[k] == 1:
        for i in range(len(data)):
            if i > k and i % k == 0:
                data[i] = 0

# 素数一覧を表示したい為、リストdataの要素が１の添字（つまり素数）をfooに代入。
# 素数の数も表示したい為、変数countで素数の数を数える。
foo = ''
count = 0
for i in range(len(data)):
    if i > 1 and data[i] == 1:
        foo += str(i) + ','
        count += 1

print('素数の一覧 ' + foo)
print('素数の数は「' + str(count) + '」です。')