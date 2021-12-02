import pandas as pd
df1 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
df2 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(df1.shape,df2.shape)

df_concat=pd.concat([df1,df2],axis=1)
