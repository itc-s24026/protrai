import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

# 把画像文件用数字行列进行变换

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)

    numImage = numpy.asarray(grayImage,dtype = float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    numImage = numImage.flatten()

    print(numImage)
    return numImage

# 预测数字

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data,digits.target)
    n = clf.predict([data])
    print("预测=", n)

data = imageToData("tmp/2.png")#确认路径
predictDigits(data)
