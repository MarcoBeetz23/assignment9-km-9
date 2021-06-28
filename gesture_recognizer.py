import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import  QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPainter, QPen

from QDrawWidget import QDrawWidget

class GestureWindow(QMainWindow):
    def __init__(self, port=5700):
        super(GestureWindow, self).__init__()
        self.setGeometry(700, 100, 500, 500)
        self.initUIComponents()

    def initUIComponents(self):
        self.drawing_area = QDrawWidget()

def main():
    app = QApplication(sys.argv)
    win = GestureWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()