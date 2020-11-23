# https://wikidocs.net/33823

## Ex 5-17. QTimeEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        # QTimeEdit 클래스를 이용해서 시간 편집 위젯(timeedit)을 하나 만들어줍니다.
        #
        # setTime 메서드에 QTime.currentTime()를 입력해서 프로그램이
        # 실행될 때 현재 시간으로 표시되도록 합니다.
        #
        # setTimeRange 이용하면 사용자가 선택할 수 있는 시간의 범위를 제한할 수 있습니다.
        #
        # 최소 시간은 디폴트로 00시 00분 00초 000밀리초로 설정되어 있고,
        # 최대 시간은 23시 59분 59초 999밀리초로 설정되어 있습니다.
        timeedit.setDisplayFormat('hh:mm:ss')
        # setDisplayFormat 메서드를 이용해서 시간이 'hh:mm:ss'의
        # 형식으로 표시되도록 설정했습니다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()
        # 수직 박스 레이아웃을 이용해서 라벨과 시간 편집 위젯을 수직으로 배치하고,
        # 전체 위젯의 레이아웃으로 설정합니다.

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())