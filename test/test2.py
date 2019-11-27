import pandas as pd
col = ['a','b']
df = pd.DataFrame(columns = col)
df = df.reindex(columns = df.columns.tolist()+ ['a'])
print(df)
