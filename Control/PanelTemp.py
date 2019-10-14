import wx
from wx.lib.pubsub import pub


class MyPanel(wx.Panel):

    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        pub.subscribe(self.OnListen, 'GetSelectCol')
        



    def OnListen(self, select_col):

        self.select_col = select_col

    