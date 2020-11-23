# https://wikidocs.net/33771
## Ex 5-13. QCalenderWidget.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        # QCalenderWidget의 객체(cal)를 하나 만듭니다.
        # setGridVisible(True)로 설정하면, 날짜 사이에 그리드가 표시됩니다.
        # 날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줍니다.

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        # selectedDate는 현재 선택된 날짜 정보를 갖고 있습니다. (디폴트는 현재 날짜)
        #
        # 현재 날짜 정보를 라벨에 표시되도록 해줍니다.
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        # 수직 박스 레이아웃을 이용해서, 달력과 라벨을 수직으로 배치해줍니다.

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())
        # showDate 메서드에서, 날짜를 클릭할 때마다 라벨 텍스트가
        # 선택한 날짜(date.toString())로 표시되도록 합니다


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())