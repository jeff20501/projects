import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont

class TradingDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trading Dashboard")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()
        
        # Labels
        self.balance = 10000  # Starting balance
        self.balance_label = QLabel(f"Balance: ${self.balance}")
        self.balance_label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.balance_label)
        
        self.price_label = QLabel("Last Price: $0")
        self.price_label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.price_label)
        
        # Buy & Sell Buttons
        self.buy_button = QPushButton("BUY")
        self.buy_button.clicked.connect(self.buy)
        self.layout.addWidget(self.buy_button)
        
        self.sell_button = QPushButton("SELL")
        self.sell_button.clicked.connect(self.sell)
        self.layout.addWidget(self.sell_button)
        
        self.setLayout(self.layout)
        
        # Timer to simulate market price updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_price)
        self.timer.start(1000)  # Update every second
        
        self.current_price = 100  # Initial price

    def update_price(self):
        self.current_price += random.uniform(-5, 5)  # Simulating price movement
        self.price_label.setText(f"Last Price: ${self.current_price:.2f}")

    def buy(self):
        if self.balance >= self.current_price:
            self.balance -= self.current_price
            self.balance_label.setText(f"Balance: ${self.balance:.2f}")
            print("Bought at:", self.current_price)
        else:
            print("Not enough balance!")

    def sell(self):
        self.balance += self.current_price
        self.balance_label.setText(f"Balance: ${self.balance:.2f}")
        print("Sold at:", self.current_price)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TradingDashboard()
    window.show()
    sys.exit(app.exec())
