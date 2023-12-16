import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.button_play.clicked.connect(self.create_yellow_circle)

        self.radius = 0

    def create_yellow_circle(self):
        self.radius = random.randint(50, 200)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        painter.drawEllipse(self.width() / 2 - self.radius / 2, self.height() / 2 - self.radius / 2,
                            self.radius, self.radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
