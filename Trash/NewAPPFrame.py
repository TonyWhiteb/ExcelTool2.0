import sys,os
import wx
import  wx.lib.mixins.listctrl  as  listmix
from Control import DropTarget as DT
from Control import FileCtrl as FC
# from Control import Button as BT
from Control import PanelTemp as PT
from Frame import ListFrame as NLF

from collections import defaultdict
from wx.lib.pubsub import pub


class AppFrame(wx.Frame):

    def __init__(self,args,argc,title = 'Demo'
                                        ,file_path = None):

        super(AppFrame,self).__init__(parent = None, id =-1, title = title, size = (800,600))

        self.SetBackgroundColour(wx.WHITE)
        self.file_path = file_path
        self.filesAndLinks = list()
        self.col_dict = {}
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
        self.buttonpnl = ButtonPanel(panel, ButtonName_1= 'List Column', onButtonHandlers_1= self.OnListColButton)
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
    def OnListen(self,index,select_col):
    
        self.filedropctrl.SetItem(index,3,str(len(select_col)))


    def OnFilesDropped(self, filenameDropDict):
       
        dropTarget = self.filedropctrl
        
        dropCoord = filenameDropDict[ 'coord' ]                 # Not used as yet.
        pathList = filenameDropDict[ 'pathList' ]
        basename_list = filenameDropDict[ 'basenameList' ]     # leaf folders, not basenames !
        pathname_list = filenameDropDict[ 'pathname' ]
        filetype_list = filenameDropDict['filetype']
        col_dict = filenameDropDict['col_info']
        self.col_dict.update(col_dict)
        for index in range(len(basename_list)):
            basename = basename_list[index]
            pathname = pathname_list[index]
            filetype = filetype_list[index]
            total_col = len(col_dict[basename])
            textTuple = (pathname,basename,filetype,total_col)
            dropTarget.WriteTextTuple(textTuple)


    def OnListColButton(self, event):
       
        currRow = self.filedropctrl.GetCurrRow()
        
        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            select_type = self.filedropctrl.GetItemText(currRow,col = 2)
            col_info = self.col_dict[select_name]
            ListCol_frame = NLF.ListFrame(currRow,select_name,col_info,self.file_path)
            ListCol_frame.Show()
        except TypeError:
            self.Warn('You should select one row or drag one file at least')
        except OSError:
            self.Warn('You should select one row or drag one file at least')
        
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
        
        self.selected = []
        self.selected_id = []

        self.Bind(wx.EVT_CHECKBOX, self.OCheckItem)

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

    def OCheckItem(self,index, flag ):

        if flag == True:
            self.selected.append(self.GetItemText(index))
            self.selected_id.append(index)
        else:
            self.selected.remove(self.GetItemText(index))
            self.selected_id.remove(index)

    def getSelected_id(self):
        return  self.selected_id


class ButtonPanel(wx.Panel):

    def __init__(self,parent = None, id = -1,ButtonName_1 = None, onButtonHandlers_1 = None):

        super(ButtonPanel, self).__init__(parent = parent , id = id)
        
        # pub.subscribe(self.OnListen, 'GetSelectCol')

        Button_1 = wx.Button(self,-1,ButtonName_1)
        # Button_2 = wx.Button(self,-1,ButtonName_2)

        Button_1.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_1)
        # Button_2.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_2)

        btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerHorzSzr.Add(Button_1)
        btnPanel_innerHorzSzr.AddSpacer( 25 )
        # btnPanel_innerHorzSzr.Add(Button_2)
        # btnPanel_innerHorzSzr.AddSpacer( 25 )

        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_outerVertSzr.AddSpacer( 5 )
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
        btnPanel_outerVertSzr.AddSpacer( 5 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()