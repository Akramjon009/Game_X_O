import sys
from disayn import *
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QHBoxLayout
from PyQt5.Qt import Qt

class Game(Window):
    def __init__(self):
        super().__init__()

        self.ind = 0
        self.Lab = Label("Turn of X")
        self.Lab.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()

        self.btn = Button(" ")
        self.btn1 = Button(" ")
        self.btn2 = Button(" ")
        self.btn3 = Button(" ")
        self.btn4 = Button(" ")
        self.btn5 = Button(" ")
        self.btn6 = Button(" ")
        self.btn7 = Button(" ")
        self.btn8 = Button(" ")

        self.h_box.addWidget(self.btn)
        self.h_box.addWidget(self.btn1)
        self.h_box.addWidget(self.btn2)

        self.h_box1.addWidget(self.btn3)
        self.h_box1.addWidget(self.btn4)
        self.h_box1.addWidget(self.btn5)

        self.h_box2.addWidget(self.btn6)
        self.h_box2.addWidget(self.btn7)
        self.h_box2.addWidget(self.btn8)

        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addWidget(self.Lab)

        self.setLayout(self.v_box)

        self.btn.clicked.connect(self.btn_)
        self.btn1.clicked.connect(self.btn_1)
        self.btn2.clicked.connect(self.btn_2)
        self.btn3.clicked.connect(self.btn_3)
        self.btn4.clicked.connect(self.btn_4)
        self.btn5.clicked.connect(self.btn_5)
        self.btn6.clicked.connect(self.btn_6)
        self.btn7.clicked.connect(self.btn_7)
        self.btn8.clicked.connect(self.btn_8)

        self.winers()

    def winers(self):
        if self.ind > 3:
            if self.btn.text() == self.btn1.text() == self.btn2.text() and self.btn.text() != " ":
                w = self.btn.text()
                self.Lab.setText(w+" win")
                self.setenabl()

            elif self.btn3.text() == self.btn4.text() == self.btn5.text() and self.btn3.text() != " ":
                w = self.btn3.text()
                self.Lab.setText(w+" win")
                self.setenabl()

            elif self.btn6.text() == self.btn7.text() == self.btn8.text() and self.btn6.text() != " ":
                w = self.btn6.text()
                self.Lab.setText(w + " win")
                self.setenabl()

            elif self.btn.text() == self.btn4.text() == self.btn8.text() and self.btn.text() != " ":
                w = self.btn.text()
                self.Lab.setText(w + " win")
                self.setenabl()

            elif self.btn2.text() == self.btn4.text() == self.btn6.text() and self.btn2.text() != " ":
                w = self.btn2.text()
                self.Lab.setText(w + " win")
                self.setenabl()

            elif self.btn.text() == self.btn3.text() == self.btn6.text() and self.btn.text() != " ":
                w = self.btn2tText()
                self.Lab.setText(w + " win")
                self.setenabl()

            elif self.btn1.text() == self.btn4.text() == self.btn7.text() and self.btn1.text() != " ":
                w = self.btn2.text()
                self.Lab.setText(w + " win")
                self.setenabl()

            elif self.btn2.text() == self.btn5.text() == self.btn8.text() and self.btn2.text() != " ":
                w = self.btn2.text()
                self.Lab.setText(w + " win")
                self.setenabl()

    def btn_(self):
        if self.ind != 8:
            if self.btn.text() != "O" and self.btn.text() != "X":
                if self.ind % 2:
                    self.btn.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_1(self):
        if self.ind != 9:
            if self.btn1.text() != "O" and self.btn1.text() != "X":
                if self.ind % 2:
                    self.btn1.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn1.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_2(self):
        if self.ind != 9:
            if self.btn2.text() != "O" and self.btn2.text() != "X":
                if self.ind % 2:
                    self.btn2.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn2.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_3(self):
        if self.ind != 9:
            if self.btn3.text() != "O" and self.btn3.text() != "X":
                if self.ind % 2:
                    self.btn3.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn3.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_4(self):
        if self.ind != 9:
            if self.btn4.text() != "O" and self.btn4.text() != "X":
                if self.ind % 2:
                    self.btn4.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn4.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_5(self):
        if self.ind != 9:
            if self.btn5.text() != "O" and self.btn5.text() != "X":
                if self.ind % 2:
                    self.btn5.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn5.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()


    def btn_6(self):
        if self.ind != 9:
            if self.btn6.text() != "O" and self.btn6.text() != "X":
                if self.ind % 2:
                    self.btn6.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn6.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_7(self):
        if self.ind != 9:
            if self.btn7.text() != "O" and self.btn7.text() != "X":
                if self.ind % 2:
                    self.btn7.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn7.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not ("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def btn_8(self):
        if self.ind != 9:
            if self.btn8.text() != "O" and self.btn8.text() != "X":
                if self.ind % 2:
                    self.btn8.setText("O")
                    self.Lab.setText("Turn of X")
                else:
                    self.btn8.setText("X")
                    self.Lab.setText("Turn of O")
                self.ind += 1
                self.winers()
        if self.ind == 9 and not("win" in self.Lab.text()):
            self.Lab.setText("Draw")
            self.setenabl()

    def setenabl(self):
        self.btn.setEnabled(False)
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)
        self.btn6.setEnabled(False)
        self.btn7.setEnabled(False)
        self.btn8.setEnabled(False)




app = QApplication(sys.argv)
menu = Game()
menu.show()
sys.exit(app.exec_())