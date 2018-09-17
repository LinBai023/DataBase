import pandas as pd

df=pd.read_csv('/Users/zs/4111/DataBase/Batting.csv', encoding='utf-8', usecols=['playerID', 'AB', 'H'])
grouped=df.groupby(['playerID']).sum()
print(grouped)
