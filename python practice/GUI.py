import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        # super()로 기반 클래스의 메서드 호출
        #      super(Student, self).__init__()    # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.initUI()

    def initUI(self):

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # sys.argv 는 ... sys.argv는 프로그램 실행 시 입력된 값들을 읽어 들일 수 있는 파이썬 라이브러리이다.
    # https://wikidocs.net/36

    ex = MyApp()
    sys.exit(app.exec_())


