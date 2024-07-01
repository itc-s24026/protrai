#標準入力で受付だ金額を税込み(10%)として出力するプログラムを作成してください。

print("输入金额：")
a = int(input())

print("加税价格为", end="")
print(f"{a * 1.1}元。")

print(type(a))
