# SINTAXE
## 1. LABELS:
Os labels são usados para exibir texto estático na interface.

### CÓDIGO:
```python
import wx

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Label com wxPython")

# Cria um painel e um widget de label
panel = wx.Panel(frame, wx.ID_ANY)
label = wx.StaticText(panel, label="Este é um Label", pos=(20, 20))

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.StaticText`: Cria um label.
- `label`: Define o texto exibido pelo label.
- `wx.Panel`: Cria um painel para conter os widgets.

## 2. BOTÕES:
Os botões permitem ao usuário executar ações quando clicados.

### CÓDIGO:
```python
import wx

def on_click(event):
    print("Botão clicado!")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Botão com wxPython")

# Cria um painel e um widget de botão
panel = wx.Panel(frame, wx.ID_ANY)
button = wx.Button(panel, label="Clique Aqui", pos=(20, 20))
button.Bind(wx.EVT_BUTTON, on_click)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.Button`: Cria um botão.
- `label`: Define o texto exibido no botão.
- `Bind(wx.EVT_BUTTON, handler)`: Conecta o clique do botão a uma função.

## 3. CAIXAS DE ENTRADA DE TEXTO (TEXTCTRL):
As caixas de entrada de texto permitem ao usuário inserir texto.

### CÓDIGO:
```python
import wx

def get_text(event):
    texto = text_ctrl.GetValue()
    print(f"Você digitou: {texto}")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Entrada de Texto com wxPython")

# Cria um painel, uma caixa de entrada de texto e um botão
panel = wx.Panel(frame, wx.ID_ANY)
text_ctrl = wx.TextCtrl(panel, pos=(20, 20))
button = wx.Button(panel, label="Enviar", pos=(20, 60))
button.Bind(wx.EVT_BUTTON, get_text)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.TextCtrl`: Cria uma caixa de entrada de texto.
- `GetValue()`: Obtém o texto inserido na caixa de entrada.

## 4. CAIXAS DE SELEÇÃO (CHECKBOX):
As caixas de seleção permitem ao usuário selecionar ou desmarcar opções.

### CÓDIGO:
```python
import wx

def check_status(event):
    status = 'checked' if checkbox.GetValue() else 'unchecked'
    print(f"Checkbox está: {status}")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Checkbox com wxPython")

# Cria um painel e uma caixa de seleção
panel = wx.Panel(frame, wx.ID_ANY)
checkbox = wx.CheckBox(panel, label="Aceito os termos e condições", pos=(20, 20))
button = wx.Button(panel, label="Verificar", pos=(20, 60))
button.Bind(wx.EVT_BUTTON, check_status)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.CheckBox`: Cria uma caixa de seleção.
- `GetValue()`: Verifica se a caixa de seleção está marcada.

## 5. RADIO BUTTONS:
Os radio buttons permitem ao usuário selecionar apenas uma opção de um grupo de opções.

### CÓDIGO:
```python
import wx

def check_selection(event):
    selecao = radio1.GetLabel() if radio1.GetValue() else radio2.GetLabel()
    print(f"Você selecionou: {selecao}")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Radio Button com wxPython")

# Cria um painel e radio buttons
panel = wx.Panel(frame, wx.ID_ANY)
radio1 = wx.RadioButton(panel, label="Opção 1", pos=(20, 20))
radio2 = wx.RadioButton(panel, label="Opção 2", pos=(20, 60))
button = wx.Button(panel, label="Verificar Seleção", pos=(20, 100))
button.Bind(wx.EVT_BUTTON, check_selection)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.RadioButton`: Cria um radio button.
- `GetValue()`: Verifica se o radio button está selecionado.
- `GetLabel()`: Obtém o texto do radio button.

## 6. SLIDERS:
Os sliders permitem ao usuário selecionar um valor de um intervalo.

### CÓDIGO:
```python
import wx

def slider_changed(event):
    value = slider.GetValue()
    print(f"Valor do slider: {value}")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de Slider com wxPython")

# Cria um painel e um slider
panel = wx.Panel(frame, wx.ID_ANY)
slider = wx.Slider(panel, value=50, minValue=0, maxValue=100, pos=(20, 20), size=(250, -1), style=wx.SL_HORIZONTAL)
slider.Bind(wx.EVT_SLIDER, slider_changed)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.Slider`: Cria um slider.
- `SetRange(minValue, maxValue)`: Define o valor mínimo e máximo do slider.
- `GetValue()`: Obtém o valor atual do slider.

## 7. COMBOBOXES:
As comboboxes permitem ao usuário selecionar um valor de uma lista suspensa.

### CÓDIGO:
```python
import wx

def get_selection(event):
    selecao = combobox.GetValue()
    print(f"Você selecionou: {selecao}")

app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Exemplo de ComboBox com wxPython")

# Cria um painel e uma combobox
panel = wx.Panel(frame, wx.ID_ANY)
combobox = wx.ComboBox(panel, choices=['Opção 1', 'Opção 2', 'Opção 3'], pos=(20, 20))
button = wx.Button(panel, label="Verificar Seleção", pos=(20, 60))
button.Bind(wx.EVT_BUTTON, get_selection)

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### EXPLICAÇÃO:
- `wx.ComboBox`: Cria uma combobox.
- `SetItems(items)`: Adiciona uma lista de opções à combobox.
- `GetValue()`: Obtém o texto da opção selecionada.
