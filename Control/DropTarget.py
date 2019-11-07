import wx
import os,sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

class DropTarget(wx.FileDropTarget):
    def __init__(self,targetControl):
        self.targetControl = targetControl

        wx.FileDropTarget.__init__(self)
    # def Filetype(x):
    #     return {
    #         'errors': 1
    #         'xlsx' : 2
    #     }.get(x,2)
        self.basename_list = []
    def Process_errors(self,afile):
        for line in afile:
            col_info = {}
            afile_list = line.split('\t')
            col_info= col_info.fromkeys(afile_list)
            return col_info
    def Process_xlsx(self,afile):
        for line in afile:
            col_info = {}
            afile_list = line.split('\t')
            col_info= col_info.fromkeys(afile_list)
            return col_info
    def OnDropFiles(self, xOrd, yOrd, pathList):

        path_list = []
        basename = []
        filetype_list = []
        col_dict = {}
        for aPath in pathList :
            pathname, aBasename = os.path.split(aPath)
            namelist = aBasename.split('.')
            filetype = namelist[len(namelist)-1]

            

            os.chdir(pathname)
            method_name = 'Process_' +str(filetype)
            method = getattr(self,method_name)
            with open(aBasename) as afile:
                col_info = method(afile)
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
            for i, col in enumerate(col_info,0):
                col_dict[aBasename][col] = i
            

        filenameDropDict = {}
        filenameDropDict['coord'] = (xOrd,yOrd)
        filenameDropDict['pathList'] = pathList
        filenameDropDict['pathname'] = path_list
        filenameDropDict['basename'] = basename
        filenameDropDict['basenameList'] = self.basename_list
        filenameDropDict['filetype'] = filetype_list
        filenameDropDict['col_info'] = col_dict
        # print(self.basename_list)
        # print(col_dict)

        if (hasattr( self.targetControl, 'dropFunc' ))  and  \
           (self.targetControl.dropFunc != None) :

            # Call the callback function with the processed drop data.
            self.targetControl.dropFunc( filenameDropDict )
        
       # HIGHL: 
        # How to add a function dynamically
