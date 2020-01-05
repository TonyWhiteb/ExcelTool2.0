import sys,os
import wx
import pysnooper
import pandas as pd
import  wx.lib.mixins.listctrl  as  listmix

from collections import defaultdict
from wx.lib.pubsub import pub
from pandas import ExcelWriter
from pandas import ExcelFile

from Frame import ListFrame as NLF
from Control import DropTarget as DT
from Control import FileCtrl as FC

class AppFrame(wx.Frame):

    def __init__(self,args,argc,title = 'Demo'
                                        ,file_path = None):

        super(AppFrame,self).__init__(parent = None, id =-1, title = title, size = (800,600))

        self.SetBackgroundColour(wx.WHITE)
        self.file_path = file_path
        self.currentDirectory = os.getcwd()
        self.filesAndLinks = list()
        self.col_dict = {}
        self.col_output = []
        # self.file_list = []
        self.file_toopen = {}
        self.duplicates = {}
        self.file_dict = {}

        # panel = PT.MyPanel(self)
        panel = wx.Panel(self,-1)
        pub.subscribe(self.OnListen, 'GetSelectCol')

        self.filedropctrl = FrameListCtrl(panel,size = (550,300),style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.filedropctrl.InsertColumn(0,'File Path')
        self.filedropctrl.InsertColumn(1,'File Name')
        self.filedropctrl.InsertColumn(2,'File Type')
        self.filedropctrl.InsertColumn(3,'Number of Columns')

        helpTextTuple = (' '*40, 'Drop Files and Folders Here',' '*len('File Type')*2
                        ,' '*len('Number of Columns  ')*2)
        self.filedropctrl.Append(helpTextTuple)

        self.filedropctrl.SetDropTarget(DT.DropTarget(self.filedropctrl))
        self.filedropctrl.dropFunc = self.OnFilesDropped
        self.filedropctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(3, wx.LIST_AUTOSIZE)




        # onButtonHandlers = self.OnListColButton
        # self.buttonpnl = ButtonPanel(panel,onButtonHandlers= onButtonHandlers,size = (-1,100))
        self.buttonpnl = ButtonPanel(panel, ButtonName_1= 'Select ALL', \
                                            onButtonHandlers_1= self.onSelectALL ,\
                                            ButtonName_2= 'List Column', \
                                            onButtonHandlers_2= self.OnListColButton,\
                                            ButtonName_3= 'Combine ALL',\
                                            onButtonHandlers_3 = self.onSaveFile )
        box_h = wx.BoxSizer(wx.VERTICAL)
        box_v = wx.BoxSizer(wx.HORIZONTAL)
        box_v.AddSpacer(25)
        box_v.Add(self.filedropctrl,1,wx.EXPAND)
        box_v.AddSpacer(25)
        box_v.Add(self.buttonpnl,0,wx.EXPAND)

        box_h.AddSpacer(20)
        box_h.Add(box_v,-1,wx.EXPAND)
        box_h.AddSpacer(20)

        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()
        self.Show()
    # def OnColInfo(self,col_info):
    @pysnooper.snoop('UndupList.log')
    def UndupList(self, alist):
        return list(dict.fromkeys(alist))

    def OnListen(self,file_dict):
        # print(file_dict)
        #TODO:
        # with pysnooper.snoop():
        # print(self.col_num)
        column_list = []

        for afile in file_dict.keys():
            column_list += file_dict[afile]
            if afile in self.file_dict.keys():
                self.file_dict[afile] = file_dict[afile]
        for index in range(self.col_num):
        
        # #     # with pysnooper.snoop():
            file_name = self.filedropctrl.GetItemText(index,1)
            if file_name in file_dict.keys():
                self.filedropctrl.SetItem(index,3,str(len(file_dict[file_name])))
                continue
            else:
                continue
        self.df_final = pd.DataFrame(columns = column_list)
        # print(self.file_dict)
        # self.filedropctrl.SetItem(index,3,str(len(select_col)))
    # def keys_exists(dict_test,*keys):
    #     if not isinstance(dict_test, dict):
    #         raise AttributeError('keys_exists() expects dict as first argument.')
    #     if len(keys) == 0:
    #         raise AttributeError('keys_exists() expects at least two arguments, one given.')

    #     _element = dict_test
    #     for key in keys:
    #         try:
    #             _element = _element[key]
    #         except KeyError:
    #             return False
    #     return True
    # def cols_exists(self,col_dict,col):
    #     if not isinstance(col_dict, dict):
    #         raise AttributeError('cols_exists() expects dict as first argument.')
    #     if len(col) == 0:
    #         raise AttributeError('cols_exists() expects at least two arguments, one given.')

    #     _element = col_dict
    #     for k,v in _element:
    #         for c,n in v:
    #             try:
                    
    @pysnooper.snoop('FileDrop.log')
    def OnFilesDropped(self, filenameDropDict):
       
        dropTarget = self.filedropctrl
        
        dropCoord = filenameDropDict[ 'coord' ]                 # Not used as yet.
        pathList = filenameDropDict[ 'pathList' ]
        basename = filenameDropDict[ 'basename' ]     # leaf folders, not basenames !
        basename_list = filenameDropDict['basenameList']
        pathname_list = filenameDropDict[ 'pathname' ]
        filetype_list = filenameDropDict['filetype']
        col_dict = filenameDropDict['col_info']
        self.col_dict.update(col_dict)
        # if len(basename_list) == 1:

        #     self.col_output = list(self.col_dict[basename_list[0]].keys())
        #     df_col = pd.DataFrame(columns = self.col_output)
        #     print(self.col_output)
        # elif len(basename_list) > 1:
        #     print(self.col_output)
        #     col_update = list(self.col_dict[basename_list[-1]].keys())
        #     alist = self.col_output + col_update
        #     # self.col_output = self.col_output.append(col_update)
        #     self.col_output = self.UndupList(self.col_output)
        #     df_col = df_col.reindex(columns = self.col_output)
        
        # self.df_all_col = df_col




        # print(self.col_dict[basename[0]].keys())
        self.file_dict[basename[0]]=  list(self.col_dict[basename[0]].keys())
        #TODO: PROCESS DUPLICATES
        # for k,v in col_dict:
        #     for col,num in v:
        #         if self.keys_exists(col_dict,k,col)
        # self.file_list.append(basename)       
        
        # print(self.file_list)
        # print(self.file_dict)
        # print(basename_list)
        self.col_num = len(basename_list)
        for index in range(len(basename)):
            # self.file_toopen[index] = basename[index]
            basename = basename[index]
            pathname = pathname_list[index]
            filetype = filetype_list[index]
            total_col = len(col_dict[basename])
            textTuple = (pathname,basename,filetype,total_col)
            dropTarget.WriteTextTuple(textTuple)
        
        # print(self.col_dict)
    # def ReadFile(self,file_dict):
    #     pass
    # def onSelectALL(self,event):
    #     pass
    def onSelectALL(self,event):
        Button = event.GetEventObject()
        Curr_Name = Button.GetLabel()
        if Curr_Name == 'Select ALL':
            Button.SetLabel('Unselect ALL')
            # Button.Refresh()
            for i in range(self.filedropctrl.numEntries):
                self.filedropctrl.CheckItem(i,check=True)
            
        elif Curr_Name == 'Unselect ALL':
            Button.SetLabel('Select ALL')
            for i in range(self.filedropctrl.numEntries):
                self.filedropctrl.CheckItem(i,check=False)
    # def onProcessDup(self,file_toOpen):
    #     UnDup = {}
    #     for num in range(len(File_ToOpen)):

    #         select_path = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =0)
    #         select_name = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =1)
    #         select_type = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =2)
    def onSaveFile(self,event):
        file_count = self.filedropctrl.GetItemCount()
        df_final = pd.DataFrame()
        dlg = wx.FileDialog(
              self, message = "Save File As",
              defaultDir=self.currentDirectory,
              defaultFile = "",wildcard="Excel files (*.xlsx)|*.xlsx",
              style= wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        if dlg.ShowModal() == wx.ID_OK:
            final_filename = dlg.GetFilename()
            path = dlg.GetPath()
            for i in range(file_count):
                file_path = self.filedropctrl.GetItemText(i,0)
                file_name = self.filedropctrl.GetItemText(i,1)
                file_type = self.filedropctrl.GetItemText(i,2)
                if file_type == 'xlsx':
                    df_process = self.readExcel(file_name,file_path)
                    df_final = df_final.append(df_process)
            basename = os.path.split(path)
            os.chdir(basename[0])
            # print(filename)
            writer = ExcelWriter(final_filename)
            df_final.to_excel(writer,'Sheet1', index = False)
            writer.save()

        dlg.Destroy()
        

        # print(df_final)
        # for key in self.file_dict
        # print(df_final)
    @pysnooper.snoop('readExcel.log')
    def readExcel(self,filename,path):
        os.chdir(path)
        column_name = []
        column_name += self.file_dict[filename]
        df_final = pd.DataFrame(columns = column_name)
        df = pd.read_excel(filename, sheet_name= 'Sheet1')
        df_need = df.loc[:,column_name]
        # df_final = df_fianl.append(df_need)
        return df_need




    # def OnCombine(self,event):
    #     #TODO:
    #     dlg = wx.FileDialog(
    #         self, message = "Save File As",
    #         defaultDir= self.currentDirectory,
    #         defaultFile= "", wildcard= "Excel Files (*.xlsx)|*.xlsx",
    #         style= wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    #     )
    #     if dlg.ShowModal() == wx.ID_OK:
            
    #         final_filename = dlg.GetFilename()
    #         path = dlg.GetPath()
    #         file_count = self.filedropctrl.GetItemCount()
    #         column_name = []
    #         for filename in self.file_dict.keys():
    #             item_list = []
    #             for i in range(file_count):
    #                 if filename == self.filedropctrl.GetItemText(i,1):
    #                     item_list.append(self.filedropctrl.GetItemText(i,0))
    #             self.filedict 


    #     pass


    def OnUnduplicates(self,col_dict):
        UnDuplicates = {}
        for afile, col_info in self.col_dict.items():
            for col, index_col in col_info.items():
                temp_dict = {afile: index_col}
                
                if col in UnDuplicates.keys() and afile in UnDuplicates[col].keys():
                    UnDuplicates[col][afile].append(temp_dict[file_name])
                elif col in UnDuplicates.keys() and afile not in UnDuplicates[col].keys():
                    UnDuplicates[col].update(temp_dict)
                else:
                    UnDuplicates[col] = temp_dict
        return UnDuplicates
    def OnListColButton(self, event):
        File_Index_ToOpen = self.filedropctrl.getSelected_id()
        File_ToOpen = self.filedropctrl.getSelected()
        File_col_info = {}
        UnDuplicates = self.OnUnduplicates(self.col_dict)
        # File_path = {}
        # print(type(File_Index_ToOpen))
        # print(File_Index_ToOpen )
        # print(currRow)
        # FileToOpen = 
        # print(self.col_dict)
        # for afile, col_info in self.col_dict.items():
        #     for col, index_col in col_info.items():
        #         temp_dict = {afile: index_col}
                
        #         if col in UnDuplicates.keys() and afile in UnDuplicates[col].keys():
        #             UnDuplicates[col][afile].append(temp_dict[file_name])
        #         elif col in UnDuplicates.keys() and afile not in UnDuplicates[col].keys():
        #             UnDuplicates[col].update(temp_dict)
        #         else:
        #             UnDuplicates[col] = temp_dict

        for num in range(len(File_ToOpen)):
        #     # print(File_Index_ToOpen(num) )
            # currRow = File_Index_ToOpen(num)
        #     temp_dict = {}
            select_path = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =0)
            select_name = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =1)
            select_type = self.filedropctrl.GetItemText(File_Index_ToOpen[num], col =2)
            File_col_info[select_name] = self.col_dict[select_name]
            
        # # pass
        #     for col, index_col in self.col_dict[select_name].items():
        #         temp_dict[select_name] = index_col
        #         if col in UnDuplicates.keys():
        #             UnDuplicates[col][select_name] = index_col
        #         else:
        #             UnDuplicates[col] = temp_dict
                # print(temp_dict)
                # if (col  in UnDuplicates.keys()) :

                #     # UnDuplicates[col] = temp_dict
                #     UnDuplicates[col][select_name].append( index_col)
                #     print(UnDuplicates)
                #     # print(UnDuplicates)
                # else:
                #     UnDuplicates[col] = temp_dict
                #     # print(UnDuplicates)
                    # UnDuplicates[col][select_name].append( index_col) 
        
        # print(UnDuplicates)
            # File_path[select_name] = select_path
        # print(File_col_info)
        # print(type(File_col_info.keys()))
        # print(type(File_col_info.values()))
        # print(list(File_col_info.values()))
        # ListCol_frame = NLF.ListFrame(File_Index_ToOpen,File_col_info)
        # ListCol_frame.Show()
        try:
            ListCol_frame = NLF.ListFrame(File_Index_ToOpen,File_col_info)
            ListCol_frame.Show()
        except TypeError:
            self.Warn('You should select one row or drag one file at least')
        except OSError:
            self.Warn('You should select one row or drag one file at least')
        # try:
        #     select_path = self.filedropctrl.GetItemText(currRow,col = 0)
        #     select_name = self.filedropctrl.GetItemText(currRow,col = 1)
        #     select_type = self.filedropctrl.GetItemText(currRow,col = 2)
        #     col_info = self.col_dict[select_name]
        #     ListCol_frame = NLF.ListFrame(currRow,select_name,col_info,self.file_path)
        #     ListCol_frame.Show()
        # except TypeError:
        #     self.Warn('You should select one row or drag one file at least')
        # except OSError:
        #     self.Warn('You should select one row or drag one file at least')
        
    def Warn(self, message, caption = 'Warning!'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy() 
        

class FrameListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):

    def __init__(self, *args, **kwargs):
        super(FrameListCtrl, self).__init__(*args,**kwargs)
        # wx.ListCtrl.__init__(self,*args,**kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        # self.setResizeColumn(0)
        self.numCols = 4
        self.entriesList = []
        self.selected = []
        self.selected_id = []
        self.haveEntries = False
        self.numEntries = 0
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckItem)

    def WriteTextTuple(self, rowDataTuple):

        assert(len(rowDataTuple) >= self.numCols), 'Given data must have at least %d items.' %(self.numCols)

        for idx in range(self.numCols):
            assert(isinstance(rowDataTuple[idx],(bytes,str,int))),'One or both data elements are not strings or numbers.'

        self.rowDataTupleTruncated = tuple(rowDataTuple[:self.numCols])

        if (self.rowDataTupleTruncated not in self.entriesList):

            if (not self.haveEntries):
                self.DeleteAllItems()

            self.Append(self.rowDataTupleTruncated)
  
            self.entriesList.append(self.rowDataTupleTruncated)
    
            self.numEntries += 1
            self.haveEntries = True

            self.Autosize()
    # def GetEntriesList(self):
    #     return self.numEntries
    def Autosize(self):
        for colIndex in [1,2,3]:
            col_width = self.GetColumnWidth(colIndex)
            self.SetColumnWidth( colIndex, wx.LIST_AUTOSIZE )
            ColMaxWid = self.GetClientSize()[ 0 ] / 2      # Half the avaiable width.
                          # Avoid the use of "Magic Numbers".
            input_width = self.GetColumnWidth( colIndex )
            reasonableWid = max( col_width, input_width )
            finalWid = min(reasonableWid,ColMaxWid)
            self.SetColumnWidth( colIndex, reasonableWid )

    def OnCheckItem(self,index, flag ):

        if flag == True:
            self.selected.append(self.GetItemText(index,1))
            self.selected_id.append(index)
        else:
            self.selected.remove(self.GetItemText(index,1))
            self.selected_id.remove(index)

    def getSelected_id(self):
        return  self.selected_id

    def getSelected(self):
        return self.selected

    # def GetRows(self):

class ButtonPanel(wx.Panel):

    def __init__(self,parent = None, id = -1,ButtonName_1 = None, onButtonHandlers_1 = None,\
                                             ButtonName_2 = None, onButtonHandlers_2 = None,\
                                             ButtonName_3 = None, onButtonHandlers_3 = None):

        super(ButtonPanel, self).__init__(parent = parent , id = id)
        
        # pub.subscribe(self.OnListen, 'GetSelectCol')

        self.Button_1 = wx.Button(self,-1,label = ButtonName_1)
        self.Button_2 = wx.Button(self,-1,label = ButtonName_2)
        self.Button_3 = wx.Button(self,-1,label = ButtonName_3)
        # self.Button_2.SelectedName = 'Unselect ALL'

        self.Button_1.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_1)
        self.Button_2.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_2)
        self.Button_3.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_3)

        btnPanel_innerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_innerVertSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerVertSzr.Add(self.Button_1)
        btnPanel_innerVertSzr.AddSpacer( 5 )
        btnPanel_innerVertSzr.Add(self.Button_2)
        btnPanel_innerVertSzr.AddSpacer( 425 )
        btnPanel_innerVertSzr.Add(self.Button_3)

        btnPanel_innerVertSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_outerVertSzr.AddSpacer( 5 )
        btnPanel_outerVertSzr.Add( btnPanel_innerVertSzr )
        btnPanel_outerVertSzr.AddSpacer( 25 )

        # btnPanel_outerHoriSzr = wx.BoxSizer(wx.HORIZONTAL)
        # bt

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()