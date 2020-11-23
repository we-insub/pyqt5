# https://wikidocs.net/23755

# 이벤트 핸들러	설명
# keyPressEvent	키보드를 눌렀을 때 동작합니다.
# keyReleaseEvent	키보드를 눌렀다가 뗄 때 동작합니다.
# mouseDoubleClickEvent	마우스를 더블클릭할 때 동작합니다.
# mouseMoveEvent	마우스를 움직일 때 동작합니다.
# mousePressEvent	마우스를 누를 때 동작합니다.
# mouseReleaseEvent	마우스를 눌렀다가 뗄 때 동작합니다.
# moveEvent	위젯이 이동할 때 동작합니다.
# resizeEvent	위젯의 크기를 변경할 때 동작합니다.

## Ex 7-3. 이벤트 핸들러 재구성하기.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
            # keyPressEvent 이벤트 핸들러는 키보드의 이벤트를 입력으로 받습니다.
            #
            # e.key()는 어떤 키를 누르거나 뗐는지를 반환합니다.
            #
            # 'esc' 키를 눌렀다면, self.close()를 통해 위젯이 종료됩니다.
            #
            # 'F' 키 또는 'N' 키를 눌렀다면, 위젯의 크기가 최대화되거나 보통 크기가 됩니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())