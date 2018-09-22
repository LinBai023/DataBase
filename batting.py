import pandas as pd
import numpy as np

df_batting=pd.read_csv('/Users/zs/4111/DataBase/Batting.csv', encoding='utf-8', usecols=['playerID','yearID', 'AB', 'H'])
df_people=pd.read_csv('/Users/zs/4111/DataBase/People.csv', encoding='utf-8', usecols=['playerID','nameFirst','nameLast'])

#records=df_batting.groupby(['playerID', 'yearID']).sum()

#print(records)

res=df_batting[df_batting['yearID']>=1960]
print(res)
test=list(res.playerID)
res=df_batting[df_batting.playerID.isin(test)]
res2=res.groupby(['playerID']).sum()
print(res2)
res3=res2[res2['AB']>200]
print(res3)
res4=res3[['AB','H']]
#print(res4)
#res5=res4.agg(divmod(res4['AB'],res4['H']))
#res5=res4.groupby('playerID').apply(lambda x: x['AB']/x['H'])
res4['H/AB'] = res4.H / res4.AB
#print(res4)
res5=res4.sort_values(['H/AB'], ascending=[False])
print(res5)
res6=pd.merge(res5, df_people, how='inner', on='playerID')
print(res6)


