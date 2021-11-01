"""
PyQT é um toolkit desenvolvido em C++ utilizado por varios programas para
criacao de aplicacoes GUI (Interface Grafica). Tambem inclui diversas funcionalidades,
como: acesso a base de dados, threads, comunicacao de rede, etc ...
pip install pyqt5

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botao')
        self.btn.setStyleSheet('font-size: 40px; ')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        # self.btn.clicked.connect(lambda: print('Ola mundo!'))
        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa. . . .')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
