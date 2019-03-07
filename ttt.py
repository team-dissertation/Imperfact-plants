import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import math

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)

    def paintEvent(self, event):
        x = 100
        y = 100
        z = 100

        length = 20

        endx = x + length * math.cos(math.pi / 2)
        endy = y + length * math.sin(math.pi / 2)

        painter = QPainter(self)

        painter.drawLine(x, y, endx, endy)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
