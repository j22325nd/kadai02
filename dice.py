import random

total = 0  # 合計値を初期化

for i in range(10):
    x = random.randint(1, 6)
    total += x
    print(str(i + 1) + "回目：" + str(x))

average = total / 10  # 平均値を計算

print("平均値：" + str(average))

#期待される出力結果の例
"""
1回目：6
2回目：3
3回目：2
4回目：2
5回目：6
6回目：5
7回目：6
8回目：1
9回目：6
10回目：2
平均値：3.9
"""