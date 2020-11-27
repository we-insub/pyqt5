## Ex 3-9. 날짜와 시간 표시하기. https://wikidocs.net/22074

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt


from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(500)

        self.setDigitCount(8)
        self.showTime()
        self.setWindowTitle("Digital Clock")
        self.resize(300, 120)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')

        # if (time.second() % 2) == 0:
        #     text = text[:2] + ' ' + text[3:]

        # 1초에 두번 신호를 주는 출력문.
        # if (time.msec() >500):
        #     text = text[:2] + ' ' + text[3:5] + ' ' + text[6:8]

        self.display(text)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


'''

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())'''