import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer


class ClickGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click the Button Game!")
        self.setGeometry(100, 100, 400, 400)

        self.score = 0
        self.time_left = 10  # 10-second timer

        # Layout
        self.layout = QVBoxLayout()

        # Score Label
        self.score_label = QLabel(f"Score: {self.score}")
        self.layout.addWidget(self.score_label)

        # Time Label
        self.time_label = QLabel(f"Time Left: {self.time_left} sec")
        self.layout.addWidget(self.time_label)

        # Game Button
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.increase_score)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        # Timer to Move the Button Randomly
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_button)
        self.move_timer.start(500)  # Moves every 0.5 seconds

        # Game Timer
        self.game_timer = QTimer()
        self.game_timer.timeout.connect(self.update_timer)
        self.game_timer.start(1000)  # Decrease time every second

    def increase_score(self):
        """Increase score when button is clicked."""
        if self.time_left > 0:
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")

    def move_button(self):
        """Move button to a random position in the window."""
        if self.time_left > 0:
            x = random.randint(50, 300)
            y = random.randint(50, 300)
            self.button.move(x, y)

    def update_timer(self):
        """Decrease time and stop game when it reaches 0."""
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.setText(f"Time Left: {self.time_left} sec")
        else:
            self.game_timer.stop()
            self.move_timer.stop()
            self.button.setDisabled(True)
            self.button.setText("Game Over!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = ClickGame()
    game.show()
    sys.exit(app.exec())
