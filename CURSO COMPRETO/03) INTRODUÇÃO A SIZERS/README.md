# INTRODUÇÃO A SIZERS
## CONCEITO:
Sizers são uma parte fundamental da biblioteca wxPython e são utilizados para gerenciar o layout de widgets (controles) dentro de uma janela ou painel. Eles são responsáveis por determinar o posicionamento e o dimensionamento dos widgets, proporcionando uma interface flexível e responsiva. Sizers permitem que você organize os widgets de maneira horizontal, vertical, em grades ou em layouts mais complexos.

## TIPOS DE SIZERS:
1. **BoxSizer**: Organiza widgets em uma única linha ou coluna.
2. **GridSizer**: Organiza widgets em uma grade de linhas e colunas.
3. **FlexGridSizer**: Semelhante ao GridSizer, mas permite que as células da grade tenham tamanhos diferentes.
4. **GridBagSizer**: Um sizer mais flexível que permite organizar widgets em uma grade onde cada célula pode abranger várias linhas e colunas.

## EXEMPLOS DE SIZERS:
### 1. BoxSizer:
BoxSizer organiza widgets em uma única linha ou coluna. A direção é especificada ao criar o sizer (`wx.HORIZONTAL` para uma linha, `wx.VERTICAL` para uma coluna).

#### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(panel, label="Este é um label")
        sizer.Add(label, 0, wx.ALL, 5)

        textbox = wx.TextCtrl(panel)
        sizer.Add(textbox, 0, wx.ALL | wx.EXPAND, 5)

        button = wx.Button(panel, label="Clique Aqui")
        sizer.Add(button, 0, wx.ALL, 5)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de BoxSizer")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.BoxSizer(wx.VERTICAL)`: Cria um BoxSizer que organiza widgets verticalmente.
- `sizer.Add(widget, proporção, flags, border)`: Adiciona um widget ao sizer. `proporção` controla o espaço que o widget ocupa, `flags` define propriedades adicionais como `wx.ALL` para adicionar espaço em todos os lados, e `border` define a quantidade de espaço ao redor do widget.

### 2. GridSizer:
GridSizer organiza widgets em uma grade com um número fixo de linhas e colunas.

#### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.GridSizer(2, 2, 10, 10)  # 2 linhas, 2 colunas, espaçamento horizontal e vertical de 10 pixels

        label1 = wx.StaticText(panel, label="Label 1")
        label2 = wx.StaticText(panel, label="Label 2")
        textbox1 = wx.TextCtrl(panel)
        textbox2 = wx.TextCtrl(panel)

        sizer.Add(label1, 0, wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALL, 5)
        sizer.Add(textbox1, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(textbox2, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de GridSizer")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.GridSizer(rows, cols, hgap, vgap)`: Cria um GridSizer com o número especificado de linhas e colunas, e espaçamento horizontal e vertical entre os widgets.
- `sizer.Add(widget, proporção, flags, border)`: Adiciona um widget ao sizer com propriedades de layout.

### 3. FlexGridSizer:
FlexGridSizer permite que as células da grade tenham tamanhos diferentes, oferecendo mais flexibilidade.

#### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.FlexGridSizer(2, 2, 10, 10)  # 2 linhas, 2 colunas, espaçamento horizontal e vertical de 10 pixels

        label1 = wx.StaticText(panel, label="Label 1")
        label2 = wx.StaticText(panel, label="Label 2")
        textbox1 = wx.TextCtrl(panel)
        textbox2 = wx.TextCtrl(panel)

        sizer.Add(label1, 0, wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALL, 5)
        sizer.Add(textbox1, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(textbox2, 0, wx.ALL | wx.EXPAND, 5)

        # Define que as colunas 1 e 2 podem expandir
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de FlexGridSizer")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.FlexGridSizer(rows, cols, hgap, vgap)`: Cria um FlexGridSizer com o número especificado de linhas e colunas, e espaçamento horizontal e vertical entre os widgets.
- `sizer.AddGrowableCol(index)`: Permite que a coluna especificada expanda para preencher o espaço disponível.

Com esses exemplos e explicações, você deve ter uma boa base para começar a usar sizers em seus projetos wxPython.