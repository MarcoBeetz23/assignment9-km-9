import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import  QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPainter, QPen

from QDrawWidget import QDrawWidget

class GestureWindow(QMainWindow):
    def __init__(self):
        super(GestureWindow, self).__init__()
        self.setGeometry(700, 100, 800, 500)
        self.initUIComponents()

    def initUIComponents(self):
        self.drawing_area = QDrawWidget()

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Switch between record and recognition mode by pushing the buttons")
        self.label1.setMinimumSize(900, 100)
        self.label1.move(175,0)


        record_button = QtWidgets.QPushButton(self)
        record_button.setText("Record")
        record_button.setMinimumSize(150,50)
        record_button.setStyleSheet("background-color :  blue")
        record_button.move(200, 100)
        record_button.clicked.connect(self.record_button_clicked)

        recognize_button = QtWidgets.QPushButton(self)
        recognize_button.setText("Recognize")
        recognize_button.setMinimumSize(150,50)
        recognize_button.setStyleSheet("background-color : yellow")
        recognize_button.move(400, 100)
        recognize_button.clicked.connect(self.recognize_button_clicked)


    def record_button_clicked(self):
        print("record active!")

    def recognize_button_clicked(self):
        print("recognition mode activated!")


def main():
    app = QApplication(sys.argv)
    win = GestureWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()