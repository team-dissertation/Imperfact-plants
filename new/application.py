import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from new.plant import *
from new.rules import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)

    def paintEvent(self, event):

        tree_paint = Paint(FractalBinaryTree(), Point(150, 250))

        tree_paint.next_generation()
        tree_paint.next_generation()
        tree_paint.next_generation()
        tree_paint.next_generation()

        lists = tree_paint.branch
        painter = QPainter(self)

        pen = QPen(Qt.red, 1)
        painter.setPen(pen)
        for i in lists:
            painter.drawLine(i.start_point.x, i.start_point.y, i.end_point.x, i.end_point.y)

        tree_paint2 = Paint(FractalBinaryTree(), Point(200, 250))
        tree_paint2.next_generation()
        tree_paint2.next_generation()
        tree_paint2.next_generation()
        tree_paint2.next_generation()

        lists2 = tree_paint2.branch
        painter2 = QPainter(self)

        pen = QPen(Qt.green, 1)
        painter2.setPen(pen)
        for i in lists2:
            painter2.drawLine(i.start_point.x, i.start_point.y, i.end_point.x, i.end_point.y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
