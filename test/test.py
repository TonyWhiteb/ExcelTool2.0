import os

dir_test = 'D:\ExcelTool\Vision 1.0'
file_name=  'PythonExport.xlsx'

os.chdir(dir_test)

with open(file_name) as afile:
    for line in afile:
        print(line)
