# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Sat Dec 10 23:11:40 2005

import wx

def _(x): return x

class RunWinPdbDialog(wx.Dialog):
    def __init__(self, fileName, runPreviousArguments, runPreviousException, *args, **kwds):
        #todo: replace choices = [] with choices = runPreviousArguments
        # begin wxGlade: RunWinPdbDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.fileName = wx.StaticText(self, -1, _("File"))
        self.argumentsLabel = wx.StaticText(self, -1, _("Arguments"))
        self.arguments = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.exception = wx.CheckBox(self, -1, _("Show dialog to launch debugger at unhandled exceptions"))
        self.label = wx.StaticText(self, -1, _("Only one script at the time can be run with Winpdb"))
        self.cancel = wx.Button(self, wx.ID_CANCEL, _("Cancel"))
        self.ok = wx.Button(self, wx.ID_OK, _("Run"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.fileName.SetLabel("File name: "+fileName)
        self.exception.SetValue(runPreviousException)
        #self.exit.SetValue(runPreviousExit)
        
    def __set_properties(self):
        #todo: comment out self.arguments.SetSelection(-1)
        # begin wxGlade: RunWinPdbDialog.__set_properties
        self.SetTitle(_("Stani's Python Editor - Run with WinPdb"))
        self.label.Enable(False)
        self.ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RunWinPdbDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.fileName, 1, wx.ALL, 4)
        sizer_2.Add(self.argumentsLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_2.Add(self.arguments, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.exception, 0, wx.ALL, 4)
        sizer_3.Add(self.label, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_3.Add(self.cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_3.Add(self.ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

##    def onOk(self, event): # wxGlade: RunDialog.<event_handler>
##        return wx.ID_OK

# end of class RunWinPdbDialog

