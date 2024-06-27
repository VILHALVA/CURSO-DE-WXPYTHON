# LISTBOX
Para implementar uma ListBox em wxPython, que permite exibir uma lista de itens selecionáveis ​​em uma interface gráfica, podemos usar a classe `wx.ListBox`. Abaixo está um exemplo simples de como criar e utilizar uma ListBox em wxPython:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.listbox = wx.ListBox(panel, choices=['Item 1', 'Item 2', 'Item 3'],
                                  style=wx.LB_SINGLE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.listbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_LISTBOX, self.OnSelect, self.listbox)

        self.Centre()
        self.Show()

    def OnSelect(self, event):
        selected = self.listbox.GetStringSelection()
        wx.MessageBox(f'Você selecionou: {selected}', 'Seleção')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='ListBox Example')
    app.MainLoop()
```

### Explicação do Código:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Cria uma ListBox (`wx.ListBox`) com três itens de exemplo ('Item 1', 'Item 2', 'Item 3') e estilo `wx.LB_SINGLE`, que permite a seleção de um único item.
     - Configura um `wx.BoxSizer` vertical (`vbox`) para organizar a ListBox no painel.
     - Define o `vbox` como o sizer do painel (`panel.SetSizer(vbox)`).
     - Liga o evento de seleção da ListBox (`wx.EVT_LISTBOX`) ao método `OnSelect`.

2. **Método `OnSelect`**:
   - `OnSelect`: É chamado quando um item na ListBox é selecionado.
   - `GetStringSelection()`: Obtém o item selecionado na ListBox.
   - Exibe uma caixa de mensagem (`wx.MessageBox`) mostrando o item selecionado.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

Este exemplo cria uma janela com uma ListBox que exibe três itens ('Item 1', 'Item 2', 'Item 3'). Quando um item é selecionado, uma caixa de mensagem exibe o item selecionado. Você pode expandir e personalizar este exemplo adicionando mais itens à ListBox ou alterando o estilo para `wx.LB_MULTIPLE` se precisar permitir a seleção múltipla de itens.