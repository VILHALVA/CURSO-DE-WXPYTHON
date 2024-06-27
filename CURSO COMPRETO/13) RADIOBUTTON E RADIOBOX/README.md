# RADIOBUTTON E RADIOBOX
Em wxPython, você pode usar tanto `wx.RadioButton` quanto `wx.RadioBox` para criar grupos de botões de opção (radio buttons). Ambos permitem que o usuário selecione apenas uma opção de um conjunto pré-definido. A diferença principal entre eles está na forma como são apresentados e organizados na interface gráfica.

## wx.RadioButton
O `wx.RadioButton` é usado para criar botões de opção individuais que são geralmente agrupados em um `wx.Panel` ou `wx.BoxSizer` para controlar a seleção exclusiva. Aqui está um exemplo de como criar e usar `wx.RadioButton`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.rb1 = wx.RadioButton(panel, label='Opção 1', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, label='Opção 2', pos=(10, 40))
        self.rb3 = wx.RadioButton(panel, label='Opção 3', pos=(10, 70))

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClicked)

        self.Centre()
        self.Show()

    def OnRadioClicked(self, event):
        radio = event.GetEventObject()
        label = radio.GetLabel()
        print(f'Radio "{label}" selecionado')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='RadioButton Example')
    app.MainLoop()
```

### Explicação do Código `wx.RadioButton`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Cria três `wx.RadioButton` com rótulos 'Opção 1', 'Opção 2' e 'Opção 3' em posições específicas no painel.
     - Usa `style=wx.RB_GROUP` no primeiro radio button para indicar que ele é o grupo inicial, permitindo que wxPython saiba que esses botões devem ser mutuamente exclusivos.
     - Liga o evento `wx.EVT_RADIOBUTTON` de qualquer radio button ao método `OnRadioClicked`.

2. **Método `OnRadioClicked`**:
   - `OnRadioClicked`: É chamado quando qualquer radio button é selecionado.
   - `GetEventObject()`: Obtém o objeto radio button que disparou o evento.
   - `GetLabel()`: Obtém o rótulo do radio button clicado.
   - Exibe no console uma mensagem indicando qual radio button foi selecionado.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## wx.RadioBox
O `wx.RadioBox` é usado para criar um grupo de botões de opção que são organizados automaticamente em uma caixa de diálogo, geralmente dentro de um `wx.Panel`. Aqui está um exemplo de como usar `wx.RadioBox`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        choices = ['Opção 1', 'Opção 2', 'Opção 3']
        self.radio_box = wx.RadioBox(panel, label='Escolha uma opção', choices=choices, majorDimension=1,
                                     style=wx.RA_SPECIFY_COLS)

        self.Bind(wx.EVT_RADIOBOX, self.OnRadioBoxClicked)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.radio_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnRadioBoxClicked(self, event):
        selection = self.radio_box.GetStringSelection()
        print(f'Opção selecionada: {selection}')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='RadioBox Example')
    app.MainLoop()
```

## Explicação do Código `wx.RadioBox`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Define uma lista de opções (`choices`) para o `wx.RadioBox`.
     - Cria um `wx.RadioBox` com um rótulo ('Escolha uma opção'), opções definidas (`choices`), e estilo `wx.RA_SPECIFY_COLS` para organizar as opções em colunas.
     - Liga o evento `wx.EVT_RADIOBOX` do `wx.RadioBox` ao método `OnRadioBoxClicked`.

2. **Método `OnRadioBoxClicked`**:
   - `OnRadioBoxClicked`: É chamado quando qualquer opção do `wx.RadioBox` é selecionada.
   - `GetStringSelection()`: Obtém a opção selecionada atualmente no `wx.RadioBox`.
   - Exibe no console a opção selecionada pelo usuário.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## Escolha entre `wx.RadioButton` e `wx.RadioBox`:
- **wx.RadioButton**: Útil quando você precisa posicionar individualmente os botões de opção em diferentes partes da sua interface ou dentro de um `wx.BoxSizer` customizado.
  
- **wx.RadioBox**: Ideal para agrupar botões de opção em uma estrutura organizada dentro de uma caixa de diálogo ou painel, especialmente útil quando as opções são fixas e conhecidas antecipadamente.

Ambas as opções são poderosas e flexíveis, dependendo das necessidades específicas do seu projeto em wxPython.