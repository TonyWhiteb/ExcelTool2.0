import sys,os
import wx
import pandas as pd
from wx.lib.pubsub import pub
from pandas import ExcelWriter
import  wx.lib.mixins.listctrl  as  listmix
from Control import FileCtrl as fc
from Control import PanelTemp as PT
import pysnooper
from collections import Counter

class ListFrame(wx.Frame):

    def __init__(self,index,file_dict):

        wx.Frame.__init__(self,None,wx.ID_ANY,"List Columns",pos= (700,300))
        self.SetClientSize((650,400))
        # self.index = index
        panel = wx.Panel(self,-1)

        # self.col_dict = col_dict
        # self.filename = filename
        self.file_dict = file_dict
        self.index = index
        self.file_name = list(self.file_dict.keys())
        self.file_col = {}
        # self.Unduplicates = Unduplicates
        # self.col_info = list(self.file_dict.values())
        # self.file_path = file_path
        # self.filelist = []
        # self.filedict = {}

        self.list_ctrl = ListColCtrl(panel, size = (500,304),style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0,'Column Number',width=wx.LIST_AUTOSIZE_USEHEADER)
        self.list_ctrl.InsertColumn(1,'Column Name')
        self.list_ctrl.InsertColumn(2,'File Name')
        self.ListColInfo(self.file_name,self.file_dict)

        # helpTextTuple = (' '*40, 'These is no columns in this file')
        # self.list_ctrl.Append(helpTextTuple)
        self.list_ctrl.SetColumnWidth(0,wx.LIST_AUTOSIZE_USEHEADER)
        self.list_ctrl.SetColumnWidth(1,wx.LIST_AUTOSIZE_USEHEADER)
        self.list_ctrl.SetColumnWidth(2,wx.LIST_AUTOSIZE_USEHEADER)

        # onButtonHandlers = self.onSelectCol
        self.buttonpnl = ButtonPanel(panel, ButtonName_1= 'Save Columns', onButtonHandlers_1= self.onSelectCol,\
                                            ButtonName_2= 'Select ALL', onButtonHandlers_2= self.onSelectAll, \
                                            ButtonName_3= 'Unselect All', onButtonHandlers_3= self.onUnselectAll,\
                                            ButtonName_4= 'Unduplicates', onButtonHandlers_4= self.UndupALL)
        box_h = wx.BoxSizer(wx.HORIZONTAL)
        box_v = wx.BoxSizer(wx.VERTICAL)
        box_v.AddSpacer(25)
        box_v.Add(self.list_ctrl,0,wx.EXPAND)
        box_v.Add(self.buttonpnl,100,wx.EXPAND)


        box_h.AddSpacer(20)
        box_h.Add(box_v,2,wx.EXPAND)
        box_h.AddSpacer(20)
        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()
        self.Show()
    # @pysnooper.snoop('undup.log')
    def Undup(self):
        col_no = self.list_ctrl.GetItemCount()
        self.col_num = col_no
        # col_no_list = [i for i in range(col_no)]
        temp_dict = {}
        for row in range(col_no):
            temp_list = []
            temp_col = self.list_ctrl.GetItemText(row,1)
            for row_nested in range(col_no):
                if temp_col == self.list_ctrl.GetItemText(row_nested,1):
                    temp_list.append(self.list_ctrl.GetItemText(row_nested,2))
                else:
                    continue

            temp_dict[temp_col] = temp_list
        return temp_dict
    # @pysnooper.snoop('UndupALL.log')
    def UndupALL(self,event):
        UndupALL = self.Undup()
        for col in range(self.col_num):
            if self.list_ctrl.IsChecked(col) == True:
                self.list_ctrl.ToggleItem(col)
        self.list_ctrl.DeleteAllItems()
        col_insert = 0
        for col, filelist in UndupALL.items():
            strfile = ', '.join([str(item) for item in filelist])
            self.list_ctrl.InsertItem(col_insert,str(col_insert+1)+' '*10)
            self.list_ctrl.SetItem(col_insert,1,col)
            self.list_ctrl.SetItem(col_insert,2,strfile)
            col_insert = col_insert + 1



            
                
            
    def ListColInfo(self,filename,col_dict):
        ListCol_dict = {}
        col_insert = 0
        for file_name in filename:
            col_no = 0
            for col_name in self.file_dict[file_name]:
                # print(col_name)
                ListCol_dict[col_name] = []
                self.list_ctrl.InsertItem(col_insert,str(col_insert+1)+' '*10)
                self.list_ctrl.SetItem(col_insert,1,col_name)
                self.list_ctrl.SetItem(col_insert,2,file_name)
                col_insert = col_insert + 1
                col_no = col_no + 1
            self.file_col[file_name] = col_no
        # self.col_num = col_no
        self.Autosize()

    # def rmDuplicates(self,event):
    #     #TODO: NEXT 10/18/2019
        
    #     pass

        # file_name = col_dict[0]
        # col_dict = {}
        # col_dict = col_dict[1]
        # col_no = 0
        # for k in col_dict:
        #     self.list_ctrl.InsertItem(col_no,str(col_no+1)+' '*10)
        #     self.list_ctrl.SetItem(col_no,1,k)
        #     self.list_ctrl.SetItem(col_no,2,file_name)
        #     col_no = col_no + 1
        # self.Autosize()
            
        # pass
    # def ListColInfo(self,col_dict):
    #     key_list = []
    #     value_list =[]

    #     for key, value in col_dict.items():
    #         key_list.append(key)
    #         value_list.append(value)
    #     if len(key_list) == len(value_list):
    #         for i in range(len(key_list)):
    #             for k in value_list[i]:
    #                 k_list =[]
    #                 k_list.append(k)
    #                 for j in range(len(k_list)) :
    #                     self.list_ctrl.InsertItem(j,k_list[j])
    #                     self.list_ctrl.SetItem(j,1,key_list[i])

    #     self.Autosize()
    #     self.filelist = key_list
    #     self.filedict = self.filedict.fromkeys(key_list)
    #     return self.list_ctrl
    def Autosize(self):
        for colIndex in range(2):
            self.list_ctrl.SetColumnWidth(colIndex,wx.LIST_AUTOSIZE)
    
    def onUnselectAll(self,event):
        col_num = self.list_ctrl.GetItemCount()
        for col in range(col_num):
            if self.list_ctrl.IsChecked(col) == True:
                self.list_ctrl.ToggleItem(col)
    
    def onSelectAll(self,event):
        col_num = self.list_ctrl.GetItemCount()
        for col in range(col_num):
            if self.list_ctrl.IsChecked(col) == False:
                self.list_ctrl.ToggleItem(col)
        # count = 0
        # for col in range(self.col_num):
        #     if self.list_ctrl.IsChecked(col):
        #         count = count + 1
        # if count >= 1:
        #     # self.buttonpnl.Button_2.SetLabel('UnSelect All')
        #     for col in range(self.col_num):
        #         self.list_ctrl.OnCheckItemItem


        # for col in range(self.col_num):
        #     if self.list_ctrl.IsChecked(col):
        #         self.buttonpnl.Button_2.SetLabel('UnSelect All')
        #     else:
        #         self.list_ctrl.CheckItem(col)

        # if self.list_ctrl.IsChecked:

        #     for col in range(self.col_num):

        #         self.list_ctrl.CheckItem(col)

    def onSelectCol(self,event):

        file_dict = {}
        # file_list = self.file_name
        for file_name in self.file_name:
            file_dict[file_name] = []
        # col_no = 0

        self.index_select = self.list_ctrl.getSelected_id()

        for col_index in self.index_select:
            filelist = list(self.list_ctrl.GetItemText(col_index,2).split(', '))
            for file_name in filelist:
                file_dict[file_name].append(self.list_ctrl.GetItemText(col_index,1))
        #     file_list.extend(filelist)
        # file_dict = dict(Counter(file_list))
        # print(file_dict)
        pub.sendMessage( 'GetSelectCol',file_dict = file_dict)
        # print(self.index_select)
        self.Close()
        # print(self.GetParent())

        # dlg = wx.FileDialog( 
        #       self, message = "Save File As",
        #       defaultDir=self.currentDirectory,
        #       defaultFile = "",wildcard="Excel files (*.xlsx)|*.xlsx",
        #       style= wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        # )
        # if dlg.ShowModal() == wx.ID_OK:
        #     final_filename = dlg.GetFilename()
        #     path = dlg.GetPath()
        #     self.index_list = self.list_ctrl.getSelected_id()
        #     column_name = []
        #     # items = self.list_ctrl.GetItem(index_list[0], 1)
        #     for filename in self.filelist:
        #         item_list = []
        #         for i in range(len(self.index_list)):
        #             if filename == self.list_ctrl.GetItemText(self.index_list[i],1):
        #                 item_list.append(self.list_ctrl.GetItemText(self.index_list[i],0))
        #         self.filedict[filename]= item_list
        #         column_name += self.filedict[filename]
        #     column_name = list(set(column_name))
        #     df_final = pd.DataFrame(columns = column_name)
        #     for key in self.filedict:
        #         df = pd.DataFrame.from_dict(self.col_dict[key])
        #         df_need = df.loc[:,self.filedict.get(key)]
        #         df_final = df_final.append(df_need)
        #     basename = os.path.split(path)
        #     os.chdir(basename[0])
        #     # print(filename)
        #     writer = ExcelWriter(final_filename)
        #     df_final.to_excel(writer,'Sheet1', index = False)
        #     writer.save()

        # dlg.Destroy()


# class ButtonPanel(wx.Panel):

#     def __init__(self,parent = None, id = -1, onButtonHandlers = None):

#         super(ButtonPanel, self).__init__(parent = parent , id = id)

#         listALL = wx.Button(self,-1,'Comfirm!')

#         listALL.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers)

#         btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
#         btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
#         btnPanel_innerHorzSzr.Add(listALL)
#         btnPanel_innerHorzSzr.AddSpacer( 25 )

#         btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

#         btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
#         btnPanel_outerVertSzr.AddSpacer( 5 )
#         btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
#         btnPanel_outerVertSzr.AddSpacer( 5 )

#         self.SetSizer( btnPanel_outerVertSzr )
#         self.Layout()

class ListColCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):

    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self,*args,**kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        # self.setResizeColumn(0)

        self.selected = []
        self.selected_id = []

        self.Bind(wx.EVT_CHECKBOX, self.OnCheckItem)
    # def UnSelect(self,index):

    #     return self.GetItem(index).GetImage() == 0
    # #         # self.IsChecked
    # def UnSelect(self,index, flag ):

    #     if flag == True:
    #         pass
    #     else:
    #         self.IsChecked
    def OnCheckItem(self,index, flag ):

        if flag == True:
            self.selected.append(self.GetItemText(index))
            self.selected_id.append(index)
        else:
            self.selected.remove(self.GetItemText(index))
            self.selected_id.remove(index)

    def getSelected_id(self):
        return  self.selected_id


class ButtonPanel(wx.Panel):

    def __init__(self,parent = None, id = -1,ButtonName_1 = None, onButtonHandlers_1 = None,\
                                             ButtonName_2 = None, onButtonHandlers_2 = None,\
                                             ButtonName_3 = None, onButtonHandlers_3 = None,\
                                             ButtonName_4 = None, onButtonHandlers_4 = None):

        super(ButtonPanel, self).__init__(parent = parent , id = id)
        
        # pub.subscribe(self.OnListen, 'GetSelectCol')

        self.Button_1 = wx.Button(self,-1,ButtonName_1)
        self.Button_2 = wx.Button(self,-1,ButtonName_2)
        self.Button_3 = wx.Button(self,-1,ButtonName_3)
        self.Button_4 = wx.Button(self,-1,ButtonName_4)

        self.Button_1.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_1)
        self.Button_2.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_2)
        self.Button_3.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_3)
        self.Button_4.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_4)

        btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerHorzSzr.Add(self.Button_1)
        btnPanel_innerHorzSzr.AddSpacer( 25 )
        btnPanel_innerHorzSzr.Add(self.Button_2)
        btnPanel_innerHorzSzr.AddSpacer( 25 )
        btnPanel_innerHorzSzr.Add(self.Button_3)
        btnPanel_innerHorzSzr.AddSpacer( 25 )
        btnPanel_innerHorzSzr.Add(self.Button_4)
        btnPanel_innerHorzSzr.AddSpacer( 25 )

        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_outerVertSzr.AddSpacer( 5 )
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
        btnPanel_outerVertSzr.AddSpacer( 5 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()