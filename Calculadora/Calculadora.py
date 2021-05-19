import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 500
        self.left = 500
        self.height = 500
        self.width = 200
        self.tittle = "Caculadora"
        self.load_main_screen()

    def load_main_screen(self):
        self.setGeometry(self.left, self.top, self.height, self.width)
        self.setWindowTitle(self.tittle)
        self.show()
    
if __name__ == '__main__':
    aplication = QApplication(sys.argv)
    window = JanelaPrincipal()
    sys.exit(aplication.exec_())