from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber


class DigitalClock(QLCDNumber): # 클래스생성 QLCD 세브세그먼트,
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent) # 초기화를 시킴

        self.setSegmentStyle(QLCDNumber.Filled) # Filled 스타일
        # 디자인중에 filled 스타일이라는 말
        #self.setSegmentStyle(QLCDNumber.Flat) # Flat Style
        #self.setSegmentStyle(QLCDNumber.Outline) # Outline Style


        self.setDigitCount(7) #원래 시 분이였는데 초를 넣기위해 짤림방지 7개로 증가
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(500)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(800, 240)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm') # mm:ss 로바꾼다면 시간이짤린다.
        #if (time.second() % 2) == 0: # 초 시간을 가지고 올수 있는 함수 time.second
        # timer.start(500) 를 1000으로바꿔야함 위의함수를 사용하려면
        if (time.msec() > 500):
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        else:
            text = text

        self.display(text)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = DigitalClock() # 디지털클락생성
    clock.show()
    sys.exit(app.exec_())