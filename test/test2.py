Source path:... d:\ExcelTool2.0\test\test.py
Starting var:.. col_list = ['col1', 'col2', 'col3', 'col4', 'col5', 'col1']
13:22:13.088199 call        21 def undup (col_list):
13:22:20.628002 line        22     temp_dict = {}
New var:....... temp_dict = {}
13:22:20.628002 line        23     col_no = len(col_list)
New var:....... col_no = 6
13:22:20.629002 line        25     for row in range(col_no):
New var:....... row = 0
13:22:20.630002 line        26         temp_list = []
New var:....... temp_list = []
13:22:20.630002 line        27         temp_col = col_list[row]
New var:....... temp_col = 'col1'
13:22:20.631001 line        28         for col in range(col_no):
New var:....... col = 0
13:22:20.632000 line        30             if temp_col == col_list[col]:
13:22:20.632000 line        31                 temp_list.append(col)
Modified var:.. temp_list = [0]
13:22:20.632999 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.632999 line        30             if temp_col == col_list[col]:
13:22:20.633998 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.633998 line        30             if temp_col == col_list[col]:
13:22:20.634999 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.634999 line        30             if temp_col == col_list[col]:
13:22:20.635998 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.635998 line        30             if temp_col == col_list[col]:
13:22:20.635998 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.636998 line        30             if temp_col == col_list[col]:
13:22:20.650989 line        31                 temp_list.append(col)
Modified var:.. temp_list = [0, 5]
13:22:20.650989 line        28         for col in range(col_no):
13:22:20.651989 line        35         temp_dict[temp_col] = temp_list
Modified var:.. temp_dict = {'col1': [0, 5]}
13:22:20.651989 line        25     for row in range(col_no):
Modified var:.. row = 1
13:22:20.659985 line        26         temp_list = []
Modified var:.. temp_list = []
13:22:20.662983 line        27         temp_col = col_list[row]
Modified var:.. temp_col = 'col2'
13:22:20.663982 line        28         for col in range(col_no):
Modified var:.. col = 0
13:22:20.663982 line        30             if temp_col == col_list[col]:
13:22:20.664984 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.664984 line        30             if temp_col == col_list[col]:
13:22:20.665981 line        31                 temp_list.append(col)
Modified var:.. temp_list = [1]
13:22:20.665981 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.666981 line        30             if temp_col == col_list[col]:
13:22:20.667980 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.667980 line        30             if temp_col == col_list[col]:
13:22:20.668979 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.668979 line        30             if temp_col == col_list[col]:
13:22:20.669980 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.669980 line        30             if temp_col == col_list[col]:
13:22:20.669980 line        28         for col in range(col_no):
13:22:20.670979 line        35         temp_dict[temp_col] = temp_list
Modified var:.. temp_dict = {'col1': [0, 5], 'col2': [1]}
13:22:20.676976 line        25     for row in range(col_no):
Modified var:.. row = 2
13:22:20.677975 line        26         temp_list = []
Modified var:.. temp_list = []
13:22:20.678974 line        27         temp_col = col_list[row]
Modified var:.. temp_col = 'col3'
13:22:20.679974 line        28         for col in range(col_no):
Modified var:.. col = 0
13:22:20.679974 line        30             if temp_col == col_list[col]:
13:22:20.680973 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.680973 line        30             if temp_col == col_list[col]:
13:22:20.681974 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.681974 line        30             if temp_col == col_list[col]:
13:22:20.682973 line        31                 temp_list.append(col)
Modified var:.. temp_list = [2]
13:22:20.682973 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.683972 line        30             if temp_col == col_list[col]:
13:22:20.683972 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.684971 line        30             if temp_col == col_list[col]:
13:22:20.684971 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.685972 line        30             if temp_col == col_list[col]:
13:22:20.685972 line        28         for col in range(col_no):
13:22:20.686970 line        35         temp_dict[temp_col] = temp_list
Modified var:.. temp_dict = {'col1': [0, 5], 'col2': [1], 'col3': [2]}
13:22:20.693967 line        25     for row in range(col_no):
Modified var:.. row = 3
13:22:20.693967 line        26         temp_list = []
Modified var:.. temp_list = []
13:22:20.694966 line        27         temp_col = col_list[row]
Modified var:.. temp_col = 'col4'
13:22:20.695965 line        28         for col in range(col_no):
Modified var:.. col = 0
13:22:20.695965 line        30             if temp_col == col_list[col]:
13:22:20.696964 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.696964 line        30             if temp_col == col_list[col]:
13:22:20.696964 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.697965 line        30             if temp_col == col_list[col]:
13:22:20.697965 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.697965 line        30             if temp_col == col_list[col]:
13:22:20.698964 line        31                 temp_list.append(col)
Modified var:.. temp_list = [3]
13:22:20.698964 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.699962 line        30             if temp_col == col_list[col]:
13:22:20.699962 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.700962 line        30             if temp_col == col_list[col]:
13:22:20.700962 line        28         for col in range(col_no):
13:22:20.700962 line        35         temp_dict[temp_col] = temp_list
Modified var:.. temp_dict = {'col1': [0, 5], 'col2': [1], 'col3': [2], 'col4': [3]}
13:22:20.701962 line        25     for row in range(col_no):
Modified var:.. row = 4
13:22:20.701962 line        26         temp_list = []
Modified var:.. temp_list = []
13:22:20.702962 line        27         temp_col = col_list[row]
Modified var:.. temp_col = 'col5'
13:22:20.710958 line        28         for col in range(col_no):
Modified var:.. col = 0
13:22:20.711956 line        30             if temp_col == col_list[col]:
13:22:20.711956 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.712957 line        30             if temp_col == col_list[col]:
13:22:20.712957 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.713955 line        30             if temp_col == col_list[col]:
13:22:20.713955 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.714955 line        30             if temp_col == col_list[col]:
13:22:20.714955 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.714955 line        30             if temp_col == col_list[col]:
13:22:20.715955 line        31                 temp_list.append(col)
Modified var:.. temp_list = [4]
13:22:20.716954 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.716954 line        30             if temp_col == col_list[col]:
13:22:20.717953 line        28         for col in range(col_no):
13:22:20.717953 line        35         temp_dict[temp_col] = temp_list
Modified var:.. temp_dict = {'col1': [0, 5], 'col2': [1], 'col3': [2], 'col4': [3], 'col5': [4]}
13:22:20.717953 line        25     for row in range(col_no):
Modified var:.. row = 5
13:22:20.718952 line        26         temp_list = []
Modified var:.. temp_list = []
13:22:20.718952 line        27         temp_col = col_list[row]
Modified var:.. temp_col = 'col1'
13:22:20.719952 line        28         for col in range(col_no):
Modified var:.. col = 0
13:22:20.720952 line        30             if temp_col == col_list[col]:
13:22:20.726948 line        31                 temp_list.append(col)
Modified var:.. temp_list = [0]
13:22:20.727947 line        28         for col in range(col_no):
Modified var:.. col = 1
13:22:20.728948 line        30             if temp_col == col_list[col]:
13:22:20.728948 line        28         for col in range(col_no):
Modified var:.. col = 2
13:22:20.729947 line        30             if temp_col == col_list[col]:
13:22:20.729947 line        28         for col in range(col_no):
Modified var:.. col = 3
13:22:20.729947 line        30             if temp_col == col_list[col]:
13:22:20.730947 line        28         for col in range(col_no):
Modified var:.. col = 4
13:22:20.730947 line        30             if temp_col == col_list[col]:
13:22:20.731945 line        28         for col in range(col_no):
Modified var:.. col = 5
13:22:20.731945 line        30             if temp_col == col_list[col]:
13:22:20.732947 line        31                 temp_list.append(col)
Modified var:.. temp_list = [0, 5]
13:22:20.732947 line        28         for col in range(col_no):
13:22:20.733945 line        35         temp_dict[temp_col] = temp_list
13:22:20.733945 line        25     for row in range(col_no):
13:22:20.733945 line        36     return temp_dict
13:22:20.734944 return      36     return temp_dict
Return value:.. {'col1': [0, 5], 'col2': [1], 'col3': [2], 'col4': [3], 'col5': [4]}