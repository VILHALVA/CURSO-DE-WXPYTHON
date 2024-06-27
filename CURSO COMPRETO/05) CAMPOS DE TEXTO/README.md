# CAMPOS DE TEXTO
## CONCEITO:
Campos de texto, também conhecidos como caixas de entrada de texto ou textctrls em wxPython, permitem aos usuários inserir e editar texto. Eles são essenciais para coletar dados do usuário, como nomes, senhas, mensagens, etc. Em wxPython, os campos de texto são criados usando a classe `wx.TextCtrl`.

## EXEMPLO BÁSICO:
Aqui está um exemplo básico de como criar e usar campos de texto em wxPython.

### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Criando um campo de texto
        self.textctrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.textctrl.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textctrl, 0, wx.ALL, 10)

        panel.SetSizer(sizer)
    
    def on_text_enter(self, event):
        texto = self.textctrl.GetValue()
        print(f"Texto digitado: {texto}")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de Campo de Texto")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)`: Cria um campo de texto dentro do painel `panel`. O estilo `wx.TE_PROCESS_ENTER` permite capturar o evento Enter pressionado.
- `self.textctrl.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter)`: Liga o evento de pressionar Enter no campo de texto à função `on_text_enter`. Quando o Enter é pressionado, a função `on_text_enter` é chamada.
- `wx.BoxSizer(wx.VERTICAL)`: Cria um BoxSizer vertical para organizar widgets.
- `sizer.Add(self.textctrl, 0, wx.ALL, 10)`: Adiciona o campo de texto ao sizer com um espaço de 10 pixels em todos os lados.

## ESTILOS DE CAMPO DE TEXTO:
Você pode personalizar os campos de texto em wxPython usando diferentes estilos.

### Estilos Comuns:
- `wx.TE_MULTILINE`: Permite que o campo de texto tenha várias linhas.
- `wx.TE_PASSWORD`: Exibe os caracteres digitados como asteriscos para campos de senha.
- `wx.TE_READONLY`: Torna o campo de texto somente leitura, sem permitir edição.

### Exemplo de Uso de Estilo:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de texto de várias linhas
        multiline_textctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        sizer.Add(multiline_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        # Campo de texto de senha
        password_textctrl = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(password_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        # Campo de texto somente leitura
        readonly_textctrl = wx.TextCtrl(panel, value="Texto somente leitura", style=wx.TE_READONLY)
        sizer.Add(readonly_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de Estilos de Campo de Texto")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `style=wx.TE_MULTILINE`: Permite que o campo de texto tenha várias linhas.
- `style=wx.TE_PASSWORD`: Exibe os caracteres digitados como asteriscos para campos de senha.
- `style=wx.TE_READONLY`: Torna o campo de texto somente leitura.

Com esses exemplos, você pode criar e personalizar campos de texto em wxPython para se adequar às necessidades do seu aplicativo.