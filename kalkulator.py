import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced PyQt5 Calculator")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #2E2E2E;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.display = QLineEdit()
        self.display.setFont(QFont('Arial', 24))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.display.setStyleSheet("color: white; background-color: #1C1C1C;")
        self.main_layout.addWidget(self.display)

        self.create_buttons()

    def create_buttons(self):
        button_layout = QGridLayout()

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
            'C': (4, 0), '(': (4, 1), ')': (4, 2), 'DEL': (4, 3)
        }

        for text, pos in buttons.items():
            button = QPushButton(text)
            button.setFont(QFont('Arial', 18))
            button.setStyleSheet(self.button_style(text))
            button.clicked.connect(self.on_button_clicked)
            button_layout.addWidget(button, *pos)

        self.main_layout.addLayout(button_layout)

    def button_style(self, text):
        operator_colors = {
            '+': '#FF5733', '-': '#FF5733', '*': '#FF5733', '/': '#FF5733',
            'C': '#E74C3C', 'DEL': '#E74C3C', '=': '#2ECC71'
        }

        if text in operator_colors:
            return f"background-color: {operator_colors[text]}; color: white;"
        else:
            return "background-color: #34495E; color: white;"

    def on_button_clicked(self):
        sender = self.sender().text()

        if sender == '=':
            try:
                expression = self.display.text()
                if any(op*2 in expression for op in "+-*/"):
                    self.display.setText("Error")
                else:
                    result = str(eval(expression))
                    self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        elif sender == 'C':
            self.display.clear()
        elif sender == 'DEL':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        else:
            if self.display.text() and self.display.text()[-1] in "+-*/" and sender in "+-*/":
                return  
            self.display.setText(self.display.text() + sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())