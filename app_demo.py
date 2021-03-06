# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# License: MIT License
# Test for Git
# ---------------------------------------------------------
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(250,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)

        bt = wx.Button(self,-1,"Hola")
        txt02 = wx.TextCtrl(self,-1,"")
        self.sz.Add(bt, 1, wx.EXPAND)
        self.sz.Add(txt02, 1, wx.EXPAND)

        self.SetBackgroundColour("#ff7700")

        txt = wx.TextCtrl(self, -1, "")
        self.sz.Add(txt, 1, wx.EXPAND)

        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()
        # This line was added by lab2dls user
        
        # Testing collab...

if __name__=='__main__':
    version = "0.1.1"
    app = wx.App()
    frame = MiAplicacion(None, u"AppDemo %s"%(version))
    app.MainLoop()
