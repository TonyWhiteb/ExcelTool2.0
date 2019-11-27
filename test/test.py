import os,sys
import pandas as pd
aPath = 'D:\\Excel Sample'

os.chdir(aPath)
 
filename =  'Sample 1.xlsx'

data = pd.read_excel(filename)
print(data.columns.values)

df_need =data.loc[:,'test_col1']
print(df_need)