# pylint: disable= multiple-imports
import sys, os
import wx
from Frame import AppFrame


if __name__ == '__main__':
    args = sys.argv
    THISPYFILE = args.pop(0)
    argc = len(args)
    path = os.path.dirname(os.path.abspath(__file__))
    app = wx.App(redirect= False)
    appFrame = AppFrame.AppFrame(args, argc, file_path= path)
    import wx.lib.inspection
    app.MainLoop()
 