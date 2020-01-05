#If you have a procedure with 10 parameters, you probably missed some.
#Group them into an object, and pass that instead
# pylint: disable= C0103
import os
import wx
import pandas as pd

import pysnooper

class DropTarget(wx.FileDropTarget):
    def __init__(self, targetControl):
        self.targetControl = targetControl

        wx.FileDropTarget.__init__(self)
    # def Filetype(x):
    #     return {
    #         'errors': 1
    #         'xlsx' : 2
    #     }.get(x,2)
        self.basename_list = []
    # @pysnooper.snoop('Process_error.log')
    def Process_errors(self, aBasename):
        with open(aBasename) as afile:
            for line in afile:
                col_info = {}
                afile_list = line.split('\t')
                col_info = col_info.fromkeys(afile_list)
                return col_info
    # @pysnooper.snoop('Process_xlsx.log')
    def Process_xlsx(self, aBasename):
        data = pd.read_excel(aBasename)
        col_info = {}
        col_info = col_info.fromkeys(data.columns.values)
        return col_info
    # @pysnooper.snoop('OnDropFiles.log')

    def OnDropFiles(self, xOrd, yOrd, pathList):

        path_list = []
        basename = []
        filetype_list = []
        col_dict = {}
        for aPath in pathList:
            pathname, aBasename = os.path.split(aPath)
            namelist = aBasename.split('.')
            filetype = namelist[len(namelist)-1]



            os.chdir(pathname)
            method_name = 'Process_' +str(filetype)
            method = getattr(self, method_name)
            col_info = method(aBasename)
            # print(col_info)
            # with open(aBasename) as afile:
                # print(type(afile))
            # if filetype == 'errors':
            #     col_info = []
            #     with open(aBasename) as afile:
            #         for line in afile:
            #             col_info= {}
            #             afile_list = line.split('\t') 
            #             col_info = col_info.fromkeys(afile_list)
            #             break
            path_list.append(pathname)
            self.basename_list.append(aBasename)
            basename.append(aBasename)
            filetype_list.append(filetype)
            col_dict[aBasename] = col_info
            for i, col in enumerate(col_info, 0):
                col_dict[aBasename][col] = i


        filenameDropDict = {}
        filenameDropDict['coord'] = (xOrd, yOrd)
        filenameDropDict['pathList'] = pathList
        filenameDropDict['pathname'] = path_list
        filenameDropDict['basename'] = basename
        filenameDropDict['basenameList'] = self.basename_list
        filenameDropDict['filetype'] = filetype_list
        filenameDropDict['col_info'] = col_dict
        # print(self.basename_list)
        # print(col_dict)

        if (hasattr(self.targetControl, 'dropFunc'))  and  \
           (self.targetControl.dropFunc is not None):

            # Call the callback function with the processed drop data.
            self.targetControl.dropFunc(filenameDropDict)

        # HIGHL: 
        # How to add a function dynamically
