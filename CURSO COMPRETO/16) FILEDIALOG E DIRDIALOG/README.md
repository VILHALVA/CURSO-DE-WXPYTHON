# FILEDIALOG E DIRDIALOG
Em wxPython, `wx.FileDialog` e `wx.DirDialog` são utilizados para interagir com o sistema de arquivos do sistema operacional, permitindo ao usuário selecionar arquivos ou diretórios. Vamos explorar como cada um deles funciona e como podem ser implementados em um exemplo prático.

## `wx.FileDialog`
O `wx.FileDialog` permite que o usuário selecione um ou mais arquivos em seu sistema de arquivos local. Aqui está um exemplo simples de como usar o `wx.FileDialog`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        open_btn = wx.Button(panel, label='Abrir Arquivo', size=(150, 30))
        open_btn.Bind(wx.EVT_BUTTON, self.OnOpen)

        vbox.Add(open_btn, proportion=1, flag=wx.CENTER | wx.TOP | wx.BOTTOM, border=20)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnOpen(self, event):
        wildcard = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, "Escolha um arquivo", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            print(f'Arquivo selecionado: {path}')

        dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='FileDialog Example')
    app.MainLoop()
```

### Explicação do Código `wx.FileDialog`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um botão (`wx.Button`) dentro de um painel (`wx.Panel`) para abrir o diálogo de seleção de arquivo.
     - Liga o evento `wx.EVT_BUTTON` do botão ao método `OnOpen`.

2. **Método `OnOpen`**:
   - `OnOpen`: É chamado quando o botão "Abrir Arquivo" é clicado.
   - `wx.FileDialog`: Cria um objeto de diálogo de arquivo com os seguintes parâmetros:
     - `self`: Janela pai para o diálogo.
     - "Escolha um arquivo": Título do diálogo.
     - `wildcard`: Filtros de arquivo, especificando os tipos de arquivos permitidos (`"Text files (*.txt)|*.txt|All files (*.*)|*.*"` neste caso).
     - `style`: Estilo do diálogo, combinando `wx.FD_OPEN` para abrir um arquivo e `wx.FD_FILE_MUST_EXIST` para garantir que o arquivo exista.
   - `ShowModal()`: Exibe o diálogo de seleção de arquivo de forma modal e aguarda a resposta do usuário.
   - `GetPath()`: Obtém o caminho completo do arquivo selecionado pelo usuário.
   - `Destroy()`: Limpa o diálogo após ser fechado.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## `wx.DirDialog`
O `wx.DirDialog` é utilizado para permitir que o usuário selecione um diretório em seu sistema de arquivos local. Aqui está um exemplo simples de como usar o `wx.DirDialog`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        open_btn = wx.Button(panel, label='Escolher Diretório', size=(150, 30))
        open_btn.Bind(wx.EVT_BUTTON, self.OnOpen)

        vbox.Add(open_btn, proportion=1, flag=wx.CENTER | wx.TOP | wx.BOTTOM, border=20)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnOpen(self, event):
        dialog = wx.DirDialog(self, "Escolha um diretório", style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            print(f'Diretório selecionado: {path}')

        dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='DirDialog Example')
    app.MainLoop()
```

### Explicação do Código `wx.DirDialog`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um botão (`wx.Button`) dentro de um painel (`wx.Panel`) para abrir o diálogo de seleção de diretório.
     - Liga o evento `wx.EVT_BUTTON` do botão ao método `OnOpen`.

2. **Método `OnOpen`**:
   - `OnOpen`: É chamado quando o botão "Escolher Diretório" é clicado.
   - `wx.DirDialog`: Cria um objeto de diálogo de diretório com os seguintes parâmetros:
     - `self`: Janela pai para o diálogo.
     - "Escolha um diretório": Título do diálogo.
     - `style`: Estilo do diálogo (`wx.DD_DEFAULT_STYLE`).
   - `ShowModal()`: Exibe o diálogo de seleção de diretório de forma modal e aguarda a resposta do usuário.
   - `GetPath()`: Obtém o caminho completo do diretório selecionado pelo usuário.
   - `Destroy()`: Limpa o diálogo após ser fechado.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

