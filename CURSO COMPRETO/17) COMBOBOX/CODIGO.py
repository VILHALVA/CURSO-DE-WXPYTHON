import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.combo = wx.ComboBox(panel, choices=['Opção 1', 'Opção 2', 'Opção 3'], style=wx.CB_DROPDOWN)
        self.button = wx.Button(panel, label='Mostrar Seleção')
        self.result_text = wx.TextCtrl(panel, style=wx.TE_READONLY)

        self.button.Bind(wx.EVT_BUTTON, self.OnShowSelection)

        vbox.Add(self.combo, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)
        vbox.Add(self.button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        vbox.Add(self.result_text, proportion=0, flag=wx.EXPAND | wx.ALL, border=20)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def OnShowSelection(self, event):
        selection = self.combo.GetValue()
        self.result_text.SetValue(f'Seleção: {selection}')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='ComboBox Example')
    app.MainLoop()
