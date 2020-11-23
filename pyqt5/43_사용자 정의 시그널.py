# https://wikidocs.net/22413

# 지정되어 있는 시그널 말고,
# 새로 원하는 시그널을 만들어서 사용할 수도 있습니다.
#
# 이번 예제에서는 pyqtSignal()을 이용해서 사용자 정의
# 시그널을 만들고, 특정 이벤트가 발생했을 때 이 시그널이 방출되도록 해보겠습니다.

## Ex 7-5. 사용자 정의 시그널.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):

    closeApp = pyqtSignal()
    # pyqtSignal()을 가지고 Communicate 클래스의 속성으로서
    # closeApp이라는 시그널을 하나 만들었습니다


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        # Communicate 클래스의 closeApp 시그널은 MyApp 클래스의 close()
        # 슬롯에 연결됩니다.

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()
        # mousePressEvent 이벤트 핸들러를 사용해서,
        # 마우스를 클릭했을 때 closeApp 시그널이 방출되도록 했습니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())