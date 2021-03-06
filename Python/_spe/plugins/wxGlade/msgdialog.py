#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.6 on Sat Sep  1 01:40:08 2007

import wx

# begin wxGlade: extracode
# end wxGlade



class MessageDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MessageDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.msg_title = wx.StaticText(self, -1, _("wxGlade message"))
        self.msg_image = wx.StaticBitmap(self, -1, (wx.ArtProvider_GetBitmap(wx.ART_TIP, wx.ART_MESSAGE_BOX, (48, 48))))
        self.msg_list = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_NO_HEADER|wx.LC_SINGLE_SEL|wx.SUNKEN_BORDER)
        self.OK = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MessageDialog.__set_properties
        self.SetTitle(_("wxGlade message"))
        self.SetSize(wx.DLG_SZE(self, (250, 112)))
        self.msg_title.SetFont(wx.Font(-1, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.msg_image.SetMinSize((48, 48))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MessageDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.msg_title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_2.Add(self.msg_image, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(self.msg_list, 1, wx.LEFT|wx.EXPAND, 10)
        sizer_1.Add(sizer_2, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        sizer_1.Add(self.OK, 0, wx.ALL|wx.ALIGN_RIGHT, 10)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MessageDialog


if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = MessageDialog(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
