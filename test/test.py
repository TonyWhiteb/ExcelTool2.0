import os,sys
import pandas as pd
aPath = 'D:\\Excel Sample'

os.chdir(aPath)
 
filename =  'Sample 1.xlsx'

data = pd.read_excel(filename)

print(data.columns.values)