#一つ目のうやり方
import pandas as pd
data = [
    [60,65,66],
    [80,85,88],
    [100,100,100]
]
df = pd.DataFrame(data)
df  


df.columns = ["国語", "数学", "英語"]
df.index = ["A太","B介","C子",]
df

#2つ目のやり方
import pandas as pd
data = [
    [60,65,66],
    [80,85,88],
    [100,100,100]
]
col = ["国語","数学","英語",]
idx = ["A太","B介","C子",]
df = pd.DataFrame(data, columns=col, index=idx)
df


#3つ目のやり方
import pandas as pd
data = {
    "国語":[60,80,100],
    "数学":[65,85,100],
    "英語":[66,88,100]
}
idx = ["A太","B介","C子",]
df = pd.DataFrame(data, index=idx)
df

import pandas as pd
df = pd.read_csv("test.csv")
df

import pandas as pd
df = pd.read_csv("test.csv", index_col=0, header=None)
df


# Untitled0.ipynb
import pandas as pd
df = pd.read_csv("test.csv")
df

import pandas as pd
df = pd.read_csv("testSJIS.csv", encoding="Shift_JIS")
df

import pandas as pd
df = pd.read_csv("test.csv", index_col=0, header=None)
df

import pandas as pd
df = df.read_csv("testNoHeader.csv", index_col=0, header=None)
df

import pandas as pd
df = pd.read_csv("test.csv", index_col=0)
df.head()

df.columns

df.index

# 列名をリストに変換する
list1 = [i for i in df.columns]
print(list1)

# インデックス名をリストに変換する
list2 = [i for i in df.index]
print(list2)

df.dtypes

len(df)

df["国語"]

df.iloc[[0]]

import pandas as pd
dfA = pd.read_csv("test.csv", index_col=0)

dfB = pd.DataFrame()
dfB["国語"] = dfA["国語"]
dfB

dfA = pd.read_csv("test.csv", index_col=0)

dfB = pd.DataFrame()
dfB = pd.concat([dfB, dfA.iloc[[0]]])
dfB

import pandas as pd
dfA = pd.read_csv("test.csv", index_col=0)

# 空のデータフレームを作成
dfB = pd.DataFrame()

dfB["国語"] = dfA["国語"]
dfB

dfA = pd.read_csv("test.csv", index_col=0)
# 空のデータフレームを作る
dfB = pd.DataFrame()
# df.iloc[[行番号]]で1行のデータを取り出す
dfB = pd.concat([dfB, dfA.iloc[[0]]])
# 表示するプリグラム
dfB

import pandas as pd
dfA = pd.read_csv("test.csv", index_col=0)
# axis=1とは列方向を意味する
dfA = dfA.drop("国語", axis=1)
dfA

# index_col=0にすることで0列目をインデックスにすることができる
dfA = pd.read_csv("test.csv", index_col=0)
dfA = dfA.drop(dfA.index[3])
dfA

dfA = pd.read_csv("test.csv", index_col=0)
dfA["国語"] > 80

dfB = dfA[dfA["国語"] > 80]
dfB

dfB = dfA[(dfA["国語"] > 80) & (dfA["数学"] > 80)]
dfB

import pandas as pd
data = {
    "国語" : [90,50,None,40],
    "数学" : [80,None,None,50]
}
idx = ["A太", "B介", "C子", "D郎"]
df = pd.DataFrame(data, index=idx)
df

dfA.isnull().sum()

dfB = dfA.dropna()
dfB

import pandas as pd
data ={
    "Aクラス" : [82,89,93,85,76],
    "Bクラス" : [100,62,82,70,86]
}
df = pd.DataFrame(data)
df

print("Aクラス=", df["Aクラス"].mean())
print("Bクラス=", df["Bクラス"].mean())

print(df.mean())
