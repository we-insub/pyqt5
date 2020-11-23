# https://wikidocs.net/32154

## Ex 5-9. QSplitter.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)
        #각 영역에 들어갈 프레임을 만들어줍니다.
        # 프레임의 형태와 그림자의 스타일을 setFrameShape과
        # setFrameShadow를 이용해서 설정할 수 있습니다.
        # 예제에서와 같이 setFrameShape에는
        # NoFrame/Box/Panel/StyledPanel/HLine/VLine/WinPanel을,
        # setFrameShadow에는 Plain/Raised/Sunken 상수를 사용할 수 있습니다.

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        # QSplitter를 이용해서 수평 방향으로 쪼개고, 왼쪽에는 midleft,
        # 오른쪽에는 midright 프레임 위젯을 넣어줍니다.
        # 다음, 수직 방향으로 쪼개고, top, splitter1, bottom 3개의 프레임 위젯을 넣어줍니다.

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        # splitter2 위젯을 수평 박스 레이아웃에 넣어주고, 전체의 레이아웃으로 설정합니다

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())