from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QPainter, QColor
from PySide6.QtSvg import QSvgGenerator
from PySide6.QtWidgets import QWidget, QFileDialog, QColorDialog

from ui_window import Ui_Window


class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path = 'test.svg'
        self.window = Ui_Window()
        self.window.setupUi(self)
        self.window.shapeComboBox.currentIndexChanged.connect(self.updateShape)
        self.window.colorButton.clicked.connect(self.updateColor)
        self.window.shapeComboBox_2.currentIndexChanged.connect(self.updateBackground)
        self.window.toolButton_2.clicked.connect(self.saveSvg)

    def saveSvg(self):
        new_path = QFileDialog.getSaveFileName(self, "Save SVG", self.path, "SVG files (*.svg)")[0]

        if new_path:
            path = new_path

            generator = QSvgGenerator()
            generator.setFileName(path)
            generator.setSize(QSize(200, 200))
            generator.setViewBox(QRect(0, 0, 200, 200))
            generator.setTitle("SVG Generator Example Drawing")
            generator.setDescription("An SVG drawing created by the SVG Generator Example provided with Qt.")

            painter = QPainter()
            painter.begin(generator)

            self.window.displayWidget.paint(painter)

            painter.end()

    def updateBackground(self, background):
        self.window.displayWidget.setBackground(self.window.displayWidget.Background[background])

    def updateColor(self):
        color = QColor(QColorDialog.getColor(self.window.displayWidget.color()))
        if color.isValid():
            self.window.displayWidget.setColor(color)

    def updateShape(self, shape):
        self.window.displayWidget.setShape(self.window.displayWidget.Shape[shape])
