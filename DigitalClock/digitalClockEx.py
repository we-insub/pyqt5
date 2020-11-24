from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtCore import QDate, Qt
from PyQt5 import uic

form_class = uic.loadUiType("form.ui")[0]

class DigitalClock(QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.date = QDate.currentDate() #
        print(QDate.currentDate())
        self.initUI()
        #self.label
        #self.lcdNumber
        #self.lineEdit

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

        self.showTime()

        self.setWindowTitle("Digital Clock")

        #self.resize(800, 240)

    def showTime(self):
        time = QTime.currentTime()
        self.date = QDate.currentDate() #
        print(self.date)
        dateStr = self.date.toString('yyyy.MM.dd')
        self.lineEdit.setText(dateStr)
        text = time.toString('hh:mm:ss')
        print(text)
        #if (time.second() % 2) == 0:
        if (time.msec() > 500 ):
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        else:
            text = text
            #tostring 시간을 읽어서 문자열 텍스트로 만들고 ,

        self.lcdNumber.display(text)

now = QDate.currentDate()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
