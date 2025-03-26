from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel
)
import sys


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator & Notes App")
        self.setGeometry(100, 100, 400, 500)

        # Layout
        self.layout = QVBoxLayout()

        # --- Calculator Section ---
        self.calc_label = QLabel("Calculator")
        self.layout.addWidget(self.calc_label)

        self.calc_input = QLineEdit()
        self.layout.addWidget(self.calc_input)

        self.calc_result = QLabel("Result: ")
        self.layout.addWidget(self.calc_result)

        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calc_button)

        # --- Notes Section ---
        self.notes_label = QLabel("Notes")
        self.layout.addWidget(self.notes_label)

        self.notes_text = QTextEdit()
        self.layout.addWidget(self.notes_text)

        self.save_button = QPushButton("Save Notes")
        self.save_button.clicked.connect(self.save_notes)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def calculate(self):
        try:
            expression = self.calc_input.text()
            result = eval(expression)  # Evaluates math expressions
            self.calc_result.setText(f"Result: {result}")
        except:
            self.calc_result.setText("Error")

    def save_notes(self):
        with open("notes.txt", "w") as file:
            file.write(self.notes_text.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())
