# https://wikidocs.net/33817

## Ex 5-16. QDateEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QDateEdit')

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # QDateEdit 클래스를 이용해서 날짜 편집 위젯을 하나 만들어줍니다.
        #
        # setDate 메서드에 QDate.currentDate()를 입력해서 프로그램이 실행될 때
        # 현재 날짜로 표시되도록 합니다.
        #
        # setMinimumDate와 setMaximumDate를 이용하면 사용자가
        # 선택할 수 있는 날짜의 범위를 제한할 수 있습니다.
        #
        # 최소 날짜는 디폴트로 1752년 9월 14일로 설정되어 있고,
        # 최대 날짜는 9999년 12월 31일로 설정되어 있습니다.
        #
        # 최소 날짜는 최소 100년 1월 1일 이상이어야합니다.


        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        # setDateRange 메서드는 setMinimumDate와 setMaximumDate를
        # 동시에 사용하는 것과 같습니다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()
        # 수직 박스 레이아웃을 이용해서 라벨과 날짜 편집 위젯을 수직으로 배치하고,
        # 전체 위젯의 레이아웃으로 설정합니다.

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())