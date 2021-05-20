import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Biblioteca para realizar o calculado das expressões
from functools import partial


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Propriedades da Janela Principal
        
        # Define nome da janela
        self.setWindowTitle("Calculadora")
        # Define as proporções da janela (Posição X, Posicão Y, Tamanho_Largura, Tamanho_Altura)
        # self.setGeometry(500, 500, 280, 500)
        
        # Não deixa o usuario alterar no tamnaho da janela
        self.setFixedSize(235, 235)
        
        # Definindo o centro do programa
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        # Definindo organização da janela
        self.generalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)
        # Chamada para a criação do Visor + Botões da calculadora
        self._createDisplay()
        self._createButtons()
        # Carrega a janela
        
    # Criação do visor
    def _createDisplay(self):
        self.display = QLineEdit()
        # Propriedades
        self.display.setFixedHeight(35)             # Tamanho da altura fixo
        self.display.setAlignment(Qt.AlignRight)    # Alinhamento do texto a direita
        self.display.setReadOnly(True)              # Somente leitura
        
        # Adicionando o visor ao layout QVBox
        self.generalLayout.addWidget(self.display)
        
    # Criação dos Botões
    def _createButtons(self):
        # Criação de um dicionário
        self.buttons = {}
        
        # Textos dos botões | posição no QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        
        # Definição da organização dos botões
        buttonsLayout = QGridLayout()
        for text, pos in buttons.items():
            self.buttons[text] = QPushButton(text)
            self.buttons[text].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[text], pos[0], pos[1])
        # Adicionando a Grid ao layout da janela principal
        self.generalLayout.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        return self.display.text()
    
    def clearDisplayText(self):
        self.setDisplayText('')
        
class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._connectSignals()
    
    # Percorre os butões para verificar se são difetentes de '=' e 'C' para fazer a chamada da função de atribuição da expressão.
    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplayText)
        
    # Adiciona valores ao visor/expressão e atualiza para ser exibido na tela.
    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
        
    def _calculateResult(self):
        result = self._model(self._view.displayText())
        self._view.setDisplayText(result)
    
def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result
    
ERROR_MSG = 'ERRO'       
        
    
if __name__ == '__main__':
    aplication = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    model = evaluateExpression
    Controller(window, model)
    sys.exit(aplication.exec_())