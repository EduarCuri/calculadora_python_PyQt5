import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Calculadora(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("calculadora.ui",self)
        self.initUi()

    def initUi(self):
        self.btn0.clicked.connect(self.obtener)
        self.btn1.clicked.connect(self.obtener1)
        self.btn2.clicked.connect(self.obtener2)
        self.btn3.clicked.connect(self.obtener3)
        self.btn4.clicked.connect(self.obtener4)
        self.btn5.clicked.connect(self.obtener5)
        self.btn6.clicked.connect(self.obtener6)
        self.btn7.clicked.connect(self.obtener7)
        self.btn8.clicked.connect(self.obtener8)
        self.btn9.clicked.connect(self.obtener9)
        self.btnpunto.clicked.connect(self.obtenerpunto)
        self.btnadicion.clicked.connect(self.obteneradicion)
        self.btnresta.clicked.connect(self.obtenerresta)
        self.btnmultiplicacion.clicked.connect(self.obtenermultiplicacion)
        self.btndivision.clicked.connect(self.obtenerdivision)
        self.btnborrar.clicked.connect(self.borrar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.btnigual.clicked.connect(self.igual)
    
    def obtener(self):
        entrada = self.valor.text()
        entrada += "0"
        self.valor.setText(entrada)

    def obtener1(self):
        entrada = self.valor.text()
        entrada += "1"
        self.valor.setText(entrada)

    def obtener2(self):
        entrada = self.valor.text()
        entrada += "2"
        self.valor.setText(entrada)

    def obtener3(self):
        entrada = self.valor.text()
        entrada += "3"
        self.valor.setText(entrada)

    def obtener4(self):
        entrada = self.valor.text()
        entrada += "4"
        self.valor.setText(entrada)

    def obtener5(self):
        entrada = self.valor.text()
        entrada += "5"
        self.valor.setText(entrada)

    def obtener6(self):
        entrada = self.valor.text()
        entrada += "6"
        self.valor.setText(entrada)

    def obtener7(self):
        entrada = self.valor.text()
        entrada += "7"
        self.valor.setText(entrada)

    def obtener8(self):
        entrada = self.valor.text()
        entrada += "8"
        self.valor.setText(entrada)

    def obtener9(self):
        entrada = self.valor.text()
        entrada += "9"
        self.valor.setText(entrada)

    def obtenerpunto(self):
        entrada = self.valor.text()
        entrada += "."
        self.valor.setText(entrada)

    def obteneradicion(self):
        entrada = self.valor.text()
        entrada += "+"
        self.valor.setText(entrada)

    def obtenerresta(self):
        entrada = self.valor.text()
        entrada += "-"
        self.valor.setText(entrada)

    def obtenermultiplicacion(self):
        entrada = self.valor.text()
        entrada += "*"
        self.valor.setText(entrada)

    def obtenerdivision(self):
        entrada = self.valor.text()
        entrada += "/"
        self.valor.setText(entrada)

    def borrar(self):
        entrada = self.valor.text()
        self.valor.setText(entrada[:len(entrada) - 1])

    def limpiar(self):
        entrada = self.valor.text()
        self.valor.setText(entrada[:0])

    def igual(self):
        ecuacion = self.valor.text()
        try:
            ans = eval(ecuacion)
            self.valor.setText(str(ans))
        except:
            self.valor.setText("Syntax error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana01 = Calculadora()
    ventana01.show()
    sys.exit(app.exec_())
