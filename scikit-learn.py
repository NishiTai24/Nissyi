pythob3 -m pip  install numpy
pythob3 -m pip  install scipy
pythob3 -m pip  install scikit-learn
pythob3 -m pip  install matplotlib


import sklean.datasets

digits = sklean.datasets.load_digits()

print("データの個数",len(digits.images))
print("画像データ",len(digits.images))
print("データの個数",len(digits.images))