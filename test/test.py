import pysnooper
col = ['col1','col2','col3','col4','col5','col1']
col_test = ['col1','col2','col3','col4','col5']
# col_no = 5
# col_no_list = [i for i in range(col_no)]


# temp_dict = {}
# for row in range(col_no):
#     temp_list = []
#     temp_col = col[row]
#     for row_nested in col_no_list:
#         if temp_col == col_test[row_nested]:
#             temp_list.append(row_nested)
#             # print(row_nested)
#             col_no_list.pop(row_nested)
#     temp_dict.update({temp_col: temp_list})

# print(temp_dict)
@pysnooper.snoop('undup.log')
def undup (col_list):
    temp_dict = {}
    col_no = len(col_list)
    # col_no_list = [i for i in range(col_no)]
    for row in range(col_no):
        # with pysnooper.snoop():
        temp_list = []
        temp_col = col_list[row]
        for col in range(col_no):
        
            if temp_col == col_list[col]:
            # with pysnooper.snoop():
                temp_list.append(col)
            else:
                continue
    # with pysnooper.snoop():
        temp_dict[temp_col] = temp_list
    return temp_dict

test = undup(col)

# @pysnooper.snoop(watch = ('test.temp_list'))





