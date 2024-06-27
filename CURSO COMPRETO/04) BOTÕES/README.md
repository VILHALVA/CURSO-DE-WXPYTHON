# BOTÕES
## CONCEITO:
Botões são elementos essenciais em interfaces gráficas que permitem aos usuários interagir com o aplicativo ao clicar neles. Em wxPython, os botões são criados usando a classe `wx.Button`. Você pode personalizar a aparência e o comportamento dos botões, como texto exibido, evento de clique e estilo.

## EXEMPLO BÁSICO:
Aqui está um exemplo básico de como criar e usar botões em wxPython.

### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Criando um botão
        self.button = wx.Button(panel, label="Clique Aqui")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 0, wx.ALL, 10)

        panel.SetSizer(sizer)
    
    def on_button_click(self, event):
        print("Botão clicado!")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de Botão")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.Button(panel, label="Clique Aqui")`: Cria um botão com o texto "Clique Aqui" dentro do painel `panel`.
- `self.button.Bind(wx.EVT_BUTTON, self.on_button_click)`: Liga o evento de clique do botão à função `on_button_click`. Quando o botão é clicado, a função `on_button_click` é chamada.
- `wx.BoxSizer(wx.VERTICAL)`: Cria um BoxSizer vertical para organizar widgets.
- `sizer.Add(self.button, 0, wx.ALL, 10)`: Adiciona o botão ao sizer com um espaço de 10 pixels em todos os lados.

## ESTILOS DE BOTÃO:
Você pode personalizar os botões em wxPython usando diferentes estilos.

### Estilos Comuns:
- `wx.BU_LEFT`: Alinha o texto do botão à esquerda.
- `wx.BU_RIGHT`: Alinha o texto do botão à direita.
- `wx.BU_TOP`: Alinha o texto do botão ao topo.
- `wx.BU_BOTTOM`: Alinha o texto do botão à base.

### Exemplo de Uso de Estilo:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Botão alinhado à esquerda
        button_left = wx.Button(panel, label="Esquerda", style=wx.BU_LEFT)
        sizer.Add(button_left, 0, wx.ALL, 10)

        # Botão alinhado à direita
        button_right = wx.Button(panel, label="Direita", style=wx.BU_RIGHT)
        sizer.Add(button_right, 0, wx.ALL, 10)

        # Botão alinhado ao topo
        button_top = wx.Button(panel, label="Topo", style=wx.BU_TOP)
        sizer.Add(button_top, 0, wx.ALL, 10)

        # Botão alinhado à base
        button_bottom = wx.Button(panel, label="Base", style=wx.BU_BOTTOM)
        sizer.Add(button_bottom, 0, wx.ALL, 10)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de Estilos de Botão")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `style=wx.BU_LEFT`, `style=wx.BU_RIGHT`, `style=wx.BU_TOP`, `style=wx.BU_BOTTOM`: Define o estilo do botão para alinhar o texto à esquerda, direita, topo ou base, respectivamente.

Com esses exemplos, você pode criar e personalizar botões em wxPython de acordo com as necessidades do seu aplicativo.