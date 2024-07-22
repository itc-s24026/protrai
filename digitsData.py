import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("数据的个数=",len(digits.images))
print("画像数据=",digits.images[1])
print("数字是什么=",digits.target[1])
