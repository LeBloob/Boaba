from PyQt5.QtCore import Qt 
from instr import *
from PyQt5.QtWidgets import(
    QApplication, QWidget, QLabel
    ,QPushButton, QHBoxLayout,
    QVBoxLayout, QLineEdit
)

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel ('Title')
        self.instruction = QLabel ('dhsaghdgsahdgsabcsabcgdsakgdagwydysaudyusabdsayudsayu')
        self.button = QPushButton ('Click')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        pass
app = QApplication([])
mw = MainWin()
app.exec_()
