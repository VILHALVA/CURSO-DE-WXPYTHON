# AGREGANDO CONTROLES
## CONCEITO:
wxPython fornece uma variedade de controles (widgets) que você pode usar para construir a interface do usuário do seu aplicativo. Esses controles incluem botões, caixas de texto, labels, caixas de seleção, radio buttons, sliders, entre outros. Cada controle é uma classe em wxPython que você pode instanciar e adicionar à sua janela principal ou a um layout.

## EXEMPLO BÁSICO:
Abaixo está um exemplo básico de como agregar diferentes controles em uma aplicação wxPython.

### CÓDIGO:
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Adicionando um label
        label = wx.StaticText(panel, label="Este é um label")
        sizer.Add(label, 0, wx.ALL, 5)

        # Adicionando uma caixa de texto
        textbox = wx.TextCtrl(panel)
        sizer.Add(textbox, 0, wx.ALL | wx.EXPAND, 5)

        # Adicionando um botão
        button = wx.Button(panel, label="Clique Aqui")
        sizer.Add(button, 0, wx.ALL, 5)

        # Adicionando uma caixa de seleção
        checkbox = wx.CheckBox(panel, label="Aceito os termos e condições")
        sizer.Add(checkbox, 0, wx.ALL, 5)

        # Adicionando um radio button
        radio1 = wx.RadioButton(panel, label="Opção 1", style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, label="Opção 2")
        sizer.Add(radio1, 0, wx.ALL, 5)
        sizer.Add(radio2, 0, wx.ALL, 5)

        # Adicionando um slider
        slider = wx.Slider(panel, minValue=0, maxValue=100)
        sizer.Add(slider, 0, wx.ALL | wx.EXPAND, 5)

        # Adicionando uma combobox
        combobox = wx.ComboBox(panel, choices=["Opção 1", "Opção 2", "Opção 3"])
        sizer.Add(combobox, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Exemplo de wxPython")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.Frame`: Cria uma janela principal.
- `wx.Panel`: Cria um painel para conter os controles.
- `wx.BoxSizer`: Organiza os controles verticalmente.
- `wx.StaticText`: Cria um label.
- `wx.TextCtrl`: Cria uma caixa de texto.
- `wx.Button`: Cria um botão.
- `wx.CheckBox`: Cria uma caixa de seleção.
- `wx.RadioButton`: Cria radio buttons.
- `wx.Slider`: Cria um slider.
- `wx.ComboBox`: Cria uma combobox.

Neste exemplo, criamos uma janela que contém um label, uma caixa de texto, um botão, uma caixa de seleção, radio buttons, um slider e uma combobox. Utilizamos um `wx.BoxSizer` para organizar os controles verticalmente na janela.