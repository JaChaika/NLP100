# NLP100本ノック
# 
# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

with open("hightemp.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines.sort(key = lambda line: line.split()[2])
print(''.join(lines))