import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from plant import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)

    def paintEvent(self, event):
        p = KochCurve()
        p.next()
        p.next()
        p.next()

        lists = p.trees
        painter = QPainter(self)

        pen = QPen(Qt.red, 1)
        painter.setPen(pen)
        for i in lists:
            painter.drawLine(i.x, i.y, i.end_x, i.end_y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
