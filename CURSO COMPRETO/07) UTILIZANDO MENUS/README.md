# UTILIZANDO MENUS
## CONCEITO:
Menus em wxPython são elementos essenciais da interface do usuário que oferecem acesso a diferentes funcionalidades e opções do aplicativo. Eles geralmente são exibidos na parte superior da janela e podem conter itens como opções de arquivo, edição, ajuda, entre outros. Em wxPython, os menus são criados usando as classes `wx.MenuBar`, `wx.Menu` e `wx.MenuItem`.

## EXEMPLO BÁSICO:
Aqui está um exemplo básico de como criar e usar menus em wxPython.

### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_NEW, "&Novo")
        file_menu.Append(wx.ID_OPEN, "&Abrir")
        file_menu.Append(wx.ID_SAVE, "&Salvar")
        file_menu.Append(wx.ID_EXIT, "&Sair")

        edit_menu = wx.Menu()
        edit_menu.Append(wx.ID_COPY, "&Copiar")
        edit_menu.Append(wx.ID_CUT, "C&ortar")
        edit_menu.Append(wx.ID_PASTE, "&Colar")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_HELP_CONTENTS, "&Conteúdo da Ajuda")
        help_menu.Append(wx.ID_ABOUT, "&Sobre")

        menubar.Append(file_menu, "&Arquivo")
        menubar.Append(edit_menu, "&Editar")
        menubar.Append(help_menu, "&Ajuda")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)

        self.Bind(wx.EVT_MENU, self.OnCopy, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.OnCut, id=wx.ID_CUT)
        self.Bind(wx.EVT_MENU, self.OnPaste, id=wx.ID_PASTE)

        self.Bind(wx.EVT_MENU, self.OnHelp, id=wx.ID_HELP_CONTENTS)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.SetSize((400, 300))
        self.SetTitle('Exemplo de Menus')
        self.Centre()

    def OnNew(self, event):
        wx.MessageBox('Novo arquivo criado!', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnOpen(self, event):
        wx.MessageBox('Abrindo arquivo...', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnSave(self, event):
        wx.MessageBox('Salvando arquivo...', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnExit(self, event):
        self.Close()

    def OnCopy(self, event):
        wx.MessageBox('Texto copiado!', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnCut(self, event):
        wx.MessageBox('Texto cortado!', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnPaste(self, event):
        wx.MessageBox('Texto colado!', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnHelp(self, event):
        wx.MessageBox('Ajuda disponível.', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnAbout(self, event):
        wx.MessageBox('Exemplo de aplicativo wxPython.', 'Sobre', wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.MenuBar()`: Cria uma barra de menu que conterá todos os menus.
- `wx.Menu()`: Cria um menu individual que será adicionado à barra de menu.
- `Append(wx.ID_xxx, "&Texto do Menu")`: Adiciona itens de menu ao menu específico. `wx.ID_xxx` são identificadores padrão para itens comuns como Novo, Abrir, Salvar, Sair, Copiar, Cortar, Colar, Ajuda e Sobre.
- `menubar.Append(menu, "&Nome do Menu")`: Adiciona um menu à barra de menu com um rótulo visível.
- `Bind(wx.EVT_MENU, self.OnFunction, id=wx.ID_xxx)`: Liga eventos de seleção de menu a funções específicas (`OnFunction` neste caso).

Este exemplo demonstra como criar menus básicos com itens comuns como Novo, Abrir, Salvar, Sair, Copiar, Cortar, Colar, Ajuda e Sobre, e como conectar esses itens a funções que realizam ações específicas quando selecionados pelo usuário.

Com essas técnicas, você pode implementar menus em wxPython para fornecer uma interface de usuário completa e funcional para seus aplicativos.