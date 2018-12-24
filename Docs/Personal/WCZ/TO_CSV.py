import pandas as pd

df = pd.read_csv('y2017nodate.csv')

s1 = (df['WEEK']-df['WEEK'].min()) / (df['WEEK'].max() - df['WEEK'].min())
df1 = df.drop(['WEEK'], axis=1)
df1.insert(0,'WEEK',s1)

s2 = (df1['TIME']-df1['TIME'].min()) / (df1['TIME'].max() - df1['TIME'].min())
df2 = df1.drop(['TIME'], axis=1)
df2.insert(1,'TIME',s2)

s3 = (df2['ID']-df2['ID'].min()) / (df2['ID'].max() - df2['ID'].min())
df3 = df2.drop(['ID'], axis=1)
df3.insert(2,'ID',s3)

s4 = (df3['NUMS']-df3['NUMS'].min()) / (df3['NUMS'].max() - df3['NUMS'].min())
df4 = df3.drop(['NUMS'], axis=1)
df4.insert(3,'NUMS',s4)

s5 = (df4['GONUMS']-df4['GONUMS'].min()) / (df4['GONUMS'].max() - df4['GONUMS'].min())
df5 = df4.drop(['GONUMS'], axis=1)
df5.insert(4,'GONUMS',s5)

s6 = (df5['REANUMS']-df5['REANUMS'].min()) / (df5['REANUMS'].max() - df5['REANUMS'].min())
df6 = df5.drop(['REANUMS'], axis=1)
df6.insert(5,'REANUMS',s6)

df6.to_csv('y2017nodate_normalzation.csv')