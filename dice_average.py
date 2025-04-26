import random 
kaisuu = [10, 100, 1000, 10000, 1000000]  # 平均値用のリスト

def roll_average(trial):
    average = 0  # 平均値の初期化
    total = 0  # サイコロの出目の合計値を記録する変数
    for n in range(trial):  # trial分だけループ処理
        x = random.randint(1, 6)  # サイコロを1回振る
        total += x  # 出目を合計に加算
    average = total / trial  # 平均値を計算
    return average  # 関数の戻り値は平均値

# リスト[kaisuu]までの平均値を求める処理
for i in kaisuu:
    print(str(i) + "回試行の平均値：" + str(roll_average(i)))


# 期待される実行結果の例
""" 
10回試行の平均値：3.8
100回試行の平均値：3.73
1000回試行の平均値：3.507
10000回試行の平均値：3.4828
1000000回試行の平均値：3.498767
"""