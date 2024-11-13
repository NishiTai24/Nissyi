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