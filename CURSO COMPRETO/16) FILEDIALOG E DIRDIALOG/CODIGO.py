import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        file_btn = wx.Button(panel, label='Abrir Arquivo', size=(150, 30))
        dir_btn = wx.Button(panel, label='Escolher Diretório', size=(150, 30))
        self.path_text = wx.TextCtrl(panel, style=wx.TE_READONLY)

        file_btn.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        dir_btn.Bind(wx.EVT_BUTTON, self.OnOpenDir)

        vbox.Add(file_btn, proportion=1, flag=wx.CENTER | wx.TOP | wx.BOTTOM, border=20)
        vbox.Add(dir_btn, proportion=1, flag=wx.CENTER | wx.TOP | wx.BOTTOM, border=20)
        vbox.Add(self.path_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def OnOpenFile(self, event):
        wildcard = "Text files (*.txt)|*.txt|Python files (*.py)|*.py|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, "Escolha um arquivo", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.path_text.SetValue(f'Arquivo selecionado:\n{path}')

        dialog.Destroy()

    def OnOpenDir(self, event):
        dialog = wx.DirDialog(self, "Escolha um diretório", style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.path_text.SetValue(f'Diretório selecionado:\n{path}')

        dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='wxPython File and Dir Dialogs')
    app.MainLoop()
