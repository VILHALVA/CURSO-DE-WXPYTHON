# SLIDER
Para criar um controle deslizante (slider) em wxPython, utilizamos a classe `wx.Slider`. Um slider permite ao usuário selecionar um valor dentro de um intervalo definido, movendo um indicador visual ao longo de uma linha horizontal ou vertical. Abaixo está um exemplo básico de como implementar um slider em wxPython:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.slider = wx.Slider(panel, value=50, minValue=0, maxValue=100,
                                style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.slider, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.slider.Bind(wx.EVT_SLIDER, self.OnSliderChange)

        self.Centre()
        self.Show()

    def OnSliderChange(self, event):
        value = self.slider.GetValue()
        print(f'Valor do slider: {value}')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='Slider Example')
    app.MainLoop()
```

### Explicação do Código:
1. **Classe `MyFrame`**:
   - `__init__`: Inicializa a janela principal (`wx.Frame`) com um título e tamanho específicos.
   - `InitUI`: Configura a interface do usuário.
     - Cria um painel (`wx.Panel`) para conter os controles.
     - Cria um slider (`wx.Slider`) horizontal (`wx.SL_HORIZONTAL`) com valor inicial (`value`) de 50, valor mínimo (`minValue`) de 0 e valor máximo (`maxValue`) de 100.
     - Define o estilo `wx.SL_LABELS` para exibir etiquetas numéricas ao longo do slider.
     - Configura um `wx.BoxSizer` vertical (`vbox`) para organizar o slider no painel.
     - Define o `vbox` como o sizer do painel (`panel.SetSizer(vbox)`).
     - Liga o evento de alteração do slider (`wx.EVT_SLIDER`) ao método `OnSliderChange`.

2. **Método `OnSliderChange`**:
   - `OnSliderChange`: É chamado quando o valor do slider é alterado pelo usuário.
   - `GetValue()`: Obtém o valor atual do slider.
   - Exibe o valor atual do slider no console (pode ser substituído por outra ação conforme necessário).

3. **Execução do Aplicativo**:
   - Cria uma instância da classe `wx.App`.
   - Cria uma instância da classe `MyFrame` como a janela principal.
   - Inicia o loop principal do aplicativo (`app.MainLoop()`).

Este exemplo cria uma janela com um slider horizontal que permite selecionar um valor de 0 a 100. Conforme o usuário move o indicador do slider, o método `OnSliderChange` é chamado para exibir o valor atual do slider. Você pode personalizar este exemplo alterando os valores mínimos e máximos do slider, seu estilo (`wx.SL_VERTICAL` para slider vertical, por exemplo), ou adicionando mais funcionalidades conforme necessário para seu aplicativo.