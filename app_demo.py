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
        self.SetBackgroundColour("#ff7700")
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    version = "0.1.1"
    app = wx.App()
    frame = MiAplicacion(None, u"AppDemo %s"%(version))
    app.MainLoop()
