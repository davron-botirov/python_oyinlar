from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

class MainClass(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(1200, 600)

        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.layout1 = QHBoxLayout(self)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button1)
        self.button1.setStyleSheet("background-color: yellow")
        self.button2.setStyleSheet("background-color: green")
        self.w1 = QWidget(self)
        self.w1.setLayout(self.layout1)

        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)

        self.button3.setStyleSheet("background-color: red")
        self.button4.setStyleSheet("background-color: pink")

        self.button3.setMinimumSize(1_000, 300)
        self.button4.setMinimumSize(1_000, 300)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(self.button3)
        self.layout2.addWidget(self.w1)
        self.layout2.addWidget(self.button4)

        self.w2 = QWidget(self)
        self.w2.setLayout(self.layout2)

        self.button1.setMinimumSize(500, 250)
        self.button2.setMinimumSize(500, 250)

        #----------------------------------

        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.button8 = QPushButton(self)

        self.button5.setMinimumSize(200, 450)
        self.button6.setMinimumSize(200, 450)
        self.button7.setMinimumSize(200, 450)
        self.button8.setMinimumSize(200, 450)

        self.button5.setStyleSheet("background-color: green")
        self.button6.setStyleSheet("background-color: yellow")
        self.button7.setStyleSheet("background-color: brown")
        self.button8.setStyleSheet("background-color: aqua")

        self.layout3 = QHBoxLayout(self)
        self.layout3.addWidget(self.button5)
        self.layout3.addWidget(self.button6)
        self.layout3.addWidget(self.button7)
        self.layout3.addWidget(self.button8)

        self.w3 = QWidget(self)
        self.w3.setLayout(self.layout3)

        self.button9 = QPushButton(self)
        self.button9.setStyleSheet("background-color: darkred")

        self.layout4 = QVBoxLayout(self)
        self.layout4.addWidget(self.w3)
        self.layout4.addWidget(self.button9)

        self.w4 = QWidget(self)
        self.w4.setLayout(self.layout4)

        self.mainlayout = QHBoxLayout(self)
        self.mainlayout.addWidget(self.w2)
        self.mainlayout.addWidget(self.w4)

        self.mainWidget = QWidget(self)
        self.mainWidget.setLayout(self.mainlayout)

        self.button9.setMinimumSize(800, 450)

        #--------------------------------------

        self.setCentralWidget(self.mainWidget)


        self.show()

app = QApplication([])
obj = MainClass()
app.exec()