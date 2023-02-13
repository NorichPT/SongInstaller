import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text = QtWidgets.QLineEdit(self)
        self.text.move(20, 20)
        self.text.resize(280, 40)

        self.button = QtWidgets.QPushButton("Enviar", self)
        self.button.move(20, 80)

        self.setGeometry(300, 300, 340, 150)
        self.setWindowTitle("PyQt5 Barra de Escrita")
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
