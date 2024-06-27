# SPINCTRL
Em wxPython, o `wx.SpinCtrl` é usado para criar um controle de spin, que é um widget de interface que permite ao usuário selecionar um valor de um intervalo específico através de botões de aumento e diminuição. É útil em situações onde você precisa que o usuário escolha um valor numérico dentro de um limite definido.

Aqui está um exemplo básico de como usar `wx.SpinCtrl`:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.spin_ctrl = wx.SpinCtrl(panel, value='0', min=0, max=100)
        self.spin_ctrl.SetRange(0, 100)  # Definindo o range (opcional)

        self.spin_ctrl.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrlChanged)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.spin_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnSpinCtrlChanged(self, event):
        value = self.spin_ctrl.GetValue()
        print(f'Valor selecionado: {value}')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='SpinCtrl Example')
    app.MainLoop()
```

## Explicação do Código:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Cria um `wx.SpinCtrl` com um valor inicial de '0', mínimo (`min`) de 0 e máximo (`max`) de 100.
     - Define o intervalo utilizando `SetRange`, embora também possa ser feito diretamente na inicialização do `wx.SpinCtrl`.
     - Liga o evento `wx.EVT_SPINCTRL` do `wx.SpinCtrl` ao método `OnSpinCtrlChanged`.

2. **Método `OnSpinCtrlChanged`**:
   - `OnSpinCtrlChanged`: É chamado quando o valor do `wx.SpinCtrl` é alterado.
   - `GetValue()`: Obtém o valor atual do `wx.SpinCtrl`.
   - Exibe no console o valor selecionado pelo usuário.

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

## Personalização e Uso Avançado:
- **Estilo e Aparência**: Você pode personalizar o estilo do `wx.SpinCtrl` para ajustar a aparência dos botões de aumento e diminuição, cores de fundo, etc.
  
- **Validação de Entrada**: É possível adicionar validação para garantir que o valor selecionado esteja dentro de limites aceitáveis para sua aplicação.

- **Integração com Outros Controles**: Combine o `wx.SpinCtrl` com outros widgets para criar interfaces mais complexas, como painéis de configuração ou formulários interativos.

O `wx.SpinCtrl` é uma ferramenta versátil para permitir que os usuários escolham números de forma intuitiva e limitada a um intervalo específico, sendo ideal para muitos tipos de aplicativos desktop que exigem entrada numérica precisa e controlada.