# MANUAL
## INSTALAÇÃO DO WXPYTHON:
### PASSO 1: INSTALAR PYTHON:
Certifique-se de ter o Python instalado. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/). Durante a instalação, marque a opção para adicionar Python ao PATH.

### PASSO 2: INSTALAR O WXPYTHON:
Você pode instalar o wxPython usando o pip. Abra um terminal ou prompt de comando e execute o seguinte comando:

```sh
pip install wxPython
```

## CONFIGURAÇÃO:
### PASSO 1: VERIFICAR A INSTALAÇÃO:
Para verificar se a instalação foi bem-sucedida, você pode executar o seguinte comando no terminal:

```sh
python -c "import wx; app = wx.App(False); frame = wx.Frame(None, wx.ID_ANY, 'Hello, wxPython!'); frame.Show(True); app.MainLoop()"
```

Se uma janela com a mensagem "Hello, wxPython!" aparecer, a instalação está correta.

## CRIANDO O PRIMEIRO PROJETO COM WXPYTHON:
### PASSO 1: CRIAR UM ARQUIVO PYTHON:
Crie um novo arquivo Python chamado `hello_wxpython.py`.

### PASSO 2: ESCREVER O CÓDIGO:
Abra o `hello_wxpython.py` em seu editor de texto ou IDE favorito e adicione o seguinte código:

```python
import wx

# Inicializa a aplicação
app = wx.App(False)

# Cria uma janela principal
frame = wx.Frame(None, wx.ID_ANY, "Meu Primeiro Aplicativo wxPython")

# Cria um painel e um widget de texto
panel = wx.Panel(frame, wx.ID_ANY)
text = wx.StaticText(panel, label="Olá, wxPython!", pos=(20, 20))

# Mostra a janela
frame.Show(True)

# Executa o loop da aplicação
app.MainLoop()
```

### PASSO 3: EXECUTAR O PROJETO:
Salve o arquivo e execute-o no terminal ou prompt de comando com o seguinte comando:

```sh
python hello_wxpython.py
```

Uma janela deve aparecer com a mensagem "Olá, wxPython!".

## ESTRUTURA DO PROJETO:
Para projetos maiores, você pode querer organizar seu código em uma estrutura de diretórios. Aqui está um exemplo básico de estrutura de diretórios para um projeto wxPython:

```
meu_projeto_wxpython/
│
├── main.py           # Ponto de entrada do aplicativo
├── gui/
│   ├── __init__.py   # Arquivo de inicialização do módulo
│   ├── main_window.py# Arquivo que define a janela principal
│
├── resources/        # Diretório para recursos como imagens, arquivos de estilo, etc.
```

### EXEMPLO DE `main_window.py`:
```python
import wx

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.SetTitle('Aplicativo wxPython Estruturado')

        panel = wx.Panel(self)
        text = wx.StaticText(panel, label="Bem-vindo ao wxPython!", pos=(20, 20))

        self.Show(True)
```

### EXEMPLO DE `main.py`
```python
import wx
from gui.main_window import MainWindow

def main():
    app = wx.App(False)
    
    window = MainWindow(None, wx.ID_ANY, '')
    window.Show(True)
    
    app.MainLoop()

if __name__ == '__main__':
    main()
```
