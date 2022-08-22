import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Calculadora(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("calculadora.ui",self)
        self.initUi()

    def initUi(self):
        self.btn_1.clicked.connect(self, uno)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana01 = Calculadora()
    ventana01.show()
    sys.exit(app.exec_())
