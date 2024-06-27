# CHECKBOX
Para criar e utilizar checkboxes (caixas de seleção) em wxPython, utilizamos a classe `wx.CheckBox`. As checkboxes permitem que os usuários selecionem uma ou mais opções de um conjunto de opções disponíveis. Abaixo está um exemplo básico de como implementar checkboxes em wxPython:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.checkbox1 = wx.CheckBox(panel, label='Opção 1', pos=(10, 10))
        self.checkbox2 = wx.CheckBox(panel, label='Opção 2', pos=(10, 40))
        self.checkbox3 = wx.CheckBox(panel, label='Opção 3', pos=(10, 70))

        self.checkbox1.Bind(wx.EVT_CHECKBOX, self.OnCheckboxClicked)
        self.checkbox2.Bind(wx.EVT_CHECKBOX, self.OnCheckboxClicked)
        self.checkbox3.Bind(wx.EVT_CHECKBOX, self.OnCheckboxClicked)

        self.Centre()
        self.Show()

    def OnCheckboxClicked(self, event):
        checkbox = event.GetEventObject()
        label = checkbox.GetLabel()
        isChecked = checkbox.GetValue()
        status = 'Marcada' if isChecked else 'Desmarcada'
        print(f'Checkbox "{label}" está {status}')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='CheckBox Example')
    app.MainLoop()
```

## Explicação do Código:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Cria três checkboxes (`wx.CheckBox`) com rótulos 'Opção 1', 'Opção 2' e 'Opção 3' em posições específicas no painel.
     - Liga o evento `wx.EVT_CHECKBOX` de cada checkbox ao método `OnCheckboxClicked`.

2. **Método `OnCheckboxClicked`**:
   - `OnCheckboxClicked`: É chamado quando uma checkbox é marcada ou desmarcada.
   - `GetEventObject()`: Obtém o objeto checkbox que disparou o evento.
   - `GetLabel()`: Obtém o rótulo da checkbox clicada.
   - `GetValue()`: Obtém o estado atual da checkbox (marcada ou desmarcada).
   - Exibe no console uma mensagem indicando se a checkbox foi marcada ou desmarcada.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

Este exemplo cria uma janela com três checkboxes onde o usuário pode selecionar várias opções. Cada checkbox está ligada a um evento que imprime no console o estado atual da checkbox (marcada ou desmarcada). Você pode expandir este exemplo adicionando mais checkboxes, personalizando seus rótulos e posicionamento, ou manipulando eventos de acordo com as necessidades do seu aplicativo.