# https://wikidocs.net/21949

## Ex 6-2. QColorDialog.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        # QColor를 사용해서 배경색인 검정색을 만들었습니다.

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        # QColorDialog를 띄우고, getColor() 메서드를 통해 색상을 저장합니다.

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
            # 색상을 선택하고 'OK' 버튼을 눌렀다면, col.isValid()의 불 값이 True이고,
            # 'Cancel' 버튼을 눌렀다면, 불 값이 False가 됩니다.
            #
            # 선택한 색상이 프레임의 배경색으로 설정됩니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())