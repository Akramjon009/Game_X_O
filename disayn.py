from PyQt5.QtWidgets import QWidget, QLabel,  QPushButton
from PyQt5.QtGui import QIcon
class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(200, 200)
        self.setStyleSheet("""background: #79AC78; 
                           border: 2px solid; 
                           border-radius: 25px;
                           font-size: 100px;
                           border-color: black; 
                           margin: 5 0""")
class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""color: black; 
                           font-size: 100px;
                           padding: 5px 
                           """)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900, 900)
        self.setStyleSheet("background: #D0E7D2")
        self.setWindowIcon(QIcon('xo_game.png'))
        