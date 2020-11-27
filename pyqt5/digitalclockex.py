from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber, QWidget
from PyQt5 import uic

form_class = uic.loadUiType("digitalclock.ui")[0]
class DigitalClock(QWidget,form_class):

   def __init__(self):
        super().__init__()
        self.setupUI()
        self.initUI()


        #self.label
        #self.LcdNumber
        #self.lineEdit

   def initUI(self):

        #timer = QTimer(self)
        #timer.timeout.connect(self.showTime)
        #timer.start(500)

        self.showTime()
        #self.setWindowTitle("Digital Clock")
        #self.resize(300, 120)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        print(text)

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