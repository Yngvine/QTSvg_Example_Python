from PySide6.QtCore import QFile, QDataStream, QRect, QLine
from PySide6.QtGui import QColor, QPainterPath, Qt, QPen, QPainter
from PySide6.QtWidgets import QWidget


class DisplayWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.Background = {0: 'Sky', 1: 'Trees', 2: 'Road'}
        self.Shape = {0: 'House', 1: 'Car'}

        self.shapeColor = QColor()
        self.shapeMap = {}

        self.moon = QPainterPath()
        self.tree = QPainterPath()
        self.car = QPainterPath()
        self.house = QPainterPath()

        file = QFile('shapes.dat')
        QFile.open(file, QFile.ReadOnly)
        stream = QDataStream(file)
        stream >> self.car >> self.house >> self.tree >> self.moon
        file.close()

        self.shapeMap[self.Shape[1]] = self.car
        self.shapeMap[self.Shape[0]] = self.house

        self.background = 'Sky'
        self.shapeColor = Qt.darkYellow
        self.shape = self.Shape[0]

    def color(self):
        return self.shapeColor

    def paint(self, painter):
        painter.setClipRect(QRect(0, 0, 200, 200))
        painter.setPen(Qt.NoPen)

        if self.background == 'Sky':
            painter.fillRect(QRect(0, 0, 200, 200), Qt.darkBlue)
            painter.translate(145, 10)
            painter.setBrush(Qt.white)
            painter.drawPath(self.moon)
            painter.translate(-145, -10)

        elif self.background == 'Trees':
            painter.fillRect(QRect(0, 0, 200, 200), Qt.darkGreen)
            painter.setBrush(Qt.green)
            painter.setPen(Qt.black)
            for y, row in zip(range(-55, 200, 50), range(0, 2000, 1)):
                if row == 2 or row == 3:
                    xs = 150
                else:
                    xs = 50
                for x in range(0, 200, xs):
                    painter.save()
                    painter.translate(x, y)
                    painter.drawPath(self.tree)
                    painter.restore()

        elif self.background == 'Road':
            painter.fillRect(QRect(0, 0, 200, 200), Qt.gray)
            painter.setPen(QPen(Qt.white, 4, Qt.DashLine))
            painter.drawLine(QLine(0, 35, 200, 35))
            painter.drawLine(QLine(0, 165, 200, 165))

        else:
            painter.fillRect(QRect(0, 0, 200, 200), Qt.darkBlue)
            painter.translate(145, 10)
            painter.setBrush(Qt.white)
            painter.drawPath(self.moon)
            painter.translate(-145, -10)

        painter.setBrush(self.shapeColor)
        painter.setPen(Qt.black)
        painter.translate(100, 100)
        painter.drawPath(self.shapeMap[self.shape])

    def setBackground(self, background):
        self.background = background
        self.update()

    def setColor(self, color):
        self.shapeColor = color
        self.update()

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.paint(painter)
        painter.end()
