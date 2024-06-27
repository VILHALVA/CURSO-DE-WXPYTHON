# COMBOBOX
Para criar um exemplo de uso de `ComboBox` (ou `wx.ComboBox`) em wxPython, vamos criar um aplicativo simples que exibe uma janela com uma `ComboBox` e um botão para mostrar a seleção feita pelo usuário. 

Certifique-se de ter o wxPython instalado. Se ainda não tiver, pode instalá-lo usando o comando `pip install wxPython`.

Aqui está o código para o projeto:

```python
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
```

## Explicação do Código:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria uma `ComboBox` (`wx.ComboBox`) com três opções pré-definidas (`choices=['Opção 1', 'Opção 2', 'Opção 3']`) e estilo `wx.CB_DROPDOWN`.
     - Cria um botão (`wx.Button`) para mostrar a seleção feita na `ComboBox`.
     - Cria um campo de texto (`wx.TextCtrl`) com estilo `wx.TE_READONLY` para exibir a seleção feita pelo usuário.

2. **Método `OnShowSelection`**:
   - `OnShowSelection`: É chamado quando o botão é clicado (`wx.EVT_BUTTON`).
     - Obtém o valor selecionado na `ComboBox` usando `self.combo.GetValue()`.
     - Exibe o valor selecionado no campo de texto (`self.result_text.SetValue()`).

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## Funcionamento do Projeto:
- Ao executar o código, uma janela será exibida contendo uma `ComboBox` com as opções "Opção 1", "Opção 2" e "Opção 3".
- O usuário pode selecionar uma das opções na `ComboBox`.
- Ao clicar no botão "Mostrar Seleção", a seleção feita na `ComboBox` será exibida no campo de texto abaixo.

Este exemplo demonstra como integrar e utilizar uma `ComboBox` em uma aplicação wxPython, permitindo ao usuário selecionar entre várias opções e responder a essa seleção de forma interativa na interface gráfica.