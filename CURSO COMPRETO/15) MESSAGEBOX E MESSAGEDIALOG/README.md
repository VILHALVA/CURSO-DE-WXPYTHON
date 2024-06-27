# MESSAGEBOX E MESSAGEDIALOG
Em wxPython, tanto `wx.MessageBox` quanto `wx.MessageDialog` são utilizados para exibir mensagens ou diálogos informativos, de erro, confirmação, entre outros, para interagir com o usuário de maneira eficaz. Vamos explorar como cada um deles pode ser utilizado:

## `wx.MessageBox`
O `wx.MessageBox` é usado para exibir uma caixa de mensagem modal que geralmente contém um texto informativo e botões para confirmação ou cancelamento. Aqui está um exemplo simples de como usá-lo:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        btn = wx.Button(panel, label='Mostrar Mensagem', pos=(50, 50))

        btn.Bind(wx.EVT_BUTTON, self.OnShowMessage)

        self.Centre()
        self.Show()

    def OnShowMessage(self, event):
        wx.MessageBox('Esta é uma caixa de mensagem simples.', 'Mensagem', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='MessageBox Example')
    app.MainLoop()
```

### Explicação do Código `wx.MessageBox`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um botão (`wx.Button`) dentro de um painel (`wx.Panel`) para acionar a exibição da mensagem.
     - Liga o evento `wx.EVT_BUTTON` do botão ao método `OnShowMessage`.

2. **Método `OnShowMessage`**:
   - `OnShowMessage`: É chamado quando o botão é clicado.
   - `wx.MessageBox`: Exibe uma caixa de mensagem modal com três parâmetros principais:
     - Texto da mensagem: "Esta é uma caixa de mensagem simples."
     - Título da janela: "Mensagem"
     - Estilo da caixa de mensagem: `wx.OK | wx.ICON_INFORMATION`, que inclui um botão OK e um ícone de informação.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

### `wx.MessageDialog`
O `wx.MessageDialog` é usado para criar um diálogo de mensagem mais personalizado, permitindo mais controle sobre o texto exibido, os botões disponíveis e as ações associadas a esses botões. Aqui está um exemplo de uso do `wx.MessageDialog`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        btn = wx.Button(panel, label='Mostrar Dialog', pos=(50, 50))

        btn.Bind(wx.EVT_BUTTON, self.OnShowDialog)

        self.Centre()
        self.Show()

    def OnShowDialog(self, event):
        dlg = wx.MessageDialog(self, 'Esta é uma caixa de diálogo personalizada.',
                               'Dialog', wx.YES_NO | wx.ICON_QUESTION)

        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            print('Você clicou em Sim.')
        else:
            print('Você clicou em Não.')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='MessageDialog Example')
    app.MainLoop()
```

### Explicação do Código `wx.MessageDialog`:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um botão (`wx.Button`) dentro de um painel (`wx.Panel`) para acionar a exibição do diálogo.
     - Liga o evento `wx.EVT_BUTTON` do botão ao método `OnShowDialog`.

2. **Método `OnShowDialog`**:
   - `OnShowDialog`: É chamado quando o botão é clicado.
   - `wx.MessageDialog`: Cria um objeto de diálogo de mensagem com os seguintes parâmetros:
     - `self`: Janela pai para o diálogo.
     - Texto da mensagem: "Esta é uma caixa de diálogo personalizada."
     - Título do diálogo: "Dialog"
     - Estilo do diálogo: `wx.YES_NO | wx.ICON_QUESTION`, que inclui botões de Sim e Não, além de um ícone de pergunta.
   - `ShowModal()`: Exibe o diálogo de mensagem de forma modal, aguardando a resposta do usuário.
   - `Destroy()`: Limpa o diálogo após ser fechado.
   - Verifica o resultado do diálogo (`result`) e imprime uma mensagem dependendo do botão clicado pelo usuário.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## Escolha entre `wx.MessageBox` e `wx.MessageDialog`:
- **`wx.MessageBox`**: Mais simples e direto para mensagens rápidas que requerem apenas um botão de confirmação.
  
- **`wx.MessageDialog`**: Mais flexível e personalizável, ideal para situações onde você precisa de botões específicos (como Sim/Não) ou mensagens mais detalhadas.

Ambos são ferramentas essenciais para interagir com o usuário em aplicativos wxPython, dependendo da complexidade e dos requisitos da mensagem a ser exibida.