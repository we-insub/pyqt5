# https://wikidocs.net/22021

## Ex 7-1. 연결하기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        # QLCDNumber 위젯은 LCD 화면과 같이 숫자를 표시합니다.
        #
        # QDial은 회전해서 값을 조절하는 위젯입니다.

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)
        # 수직 박스 레이아웃(박스 레이아웃 참고)을 하나 만들어서
        # QLCDNumber와 QDial 위젯을 넣어줍니다.
        #
        # 그리고 MyApp 위젯의 레이아웃으로 설정합니다.

        dial.valueChanged.connect(lcd.display)
        # QDial 위젯은 몇 가지 시그널을 갖고 있습니다(QSlider, QDial 참고).
        #
        # 여기서는 valueChanged 시그널을 lcd의 display 슬롯에 연결합니다.
        # display 슬롯은 숫자를 받아서 QLCDNumber 위젯에 표시하는 역할을 합니다.
        #
        # 여기서 시그널을 보내는 객체인 송신자 (sender)는 dial,
        # 시그널을 받는 객체인 수신자 (receiver)는 lcd입니다.
        #
        # 슬롯 (slot)은 시그널에 어떻게 반응할지를 구현한 메서드입니다.

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())