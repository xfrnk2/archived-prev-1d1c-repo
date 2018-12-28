import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont

class Myapp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        label1 = QLabel('First Label', self)

        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 200 ,200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())