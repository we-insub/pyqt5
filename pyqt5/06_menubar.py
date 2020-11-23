## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 아이콘 exit.png 와 exit라벨을 갖는 하나의 동작 action 을 만들고
        # 이 동작에 대한 단축키 shortcut를 정의 합니다.
        # 메뉴에 마우스를 올렸을때 상태바의 나타날 상태팁을 setstaustip()메서드를
        # 사용하여 설정하였습니다.
        exitAction.triggered.connect(qApp.quit)
        # 생성된 triggered 시그널이 Qapplication 위젯의 quit()메서드에 연결되고
        # 어플리케이션이 종료되게한다,
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        # menubar 메서드는 메뉴바를 생성합니다 이어서 file메뉴를 하나만들고 거기에
        # exit Action 동작을 추가
        # &file 이 앰퍼샌드는 간편하게 단축키를 설정하도록
        # f앞에 엔퍼샌트가 있으므로 alt + f 단축키가 된다.
        # i앞에 &넣으면 alt + i 가 된

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())