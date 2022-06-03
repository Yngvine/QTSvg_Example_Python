from PySide6.QtWidgets import QApplication

from window import Window


def main():
    app = QApplication()
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
