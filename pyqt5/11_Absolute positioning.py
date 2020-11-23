## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        # 라벨을 하나 만들고, x=20, y=20에 위치하도록 옮겨줍니다.
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        # 푸시버튼을 하나 만들고, x=80, y=13에 위치하도록 옮겨줍니다.
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 위젯의 위치를 설정하기 위해 move() 메서드를 사용합니다.
# 라벨(label1, label2)과 푸시버튼(btn1, btn2)의 x, y 좌표를 설정함으로써 위치를 조절합니다.
# 좌표계는 왼쪽 상단 모서리에서 시작합니다. x 좌표는 왼쪽에서 오른쪽으로 갈수록 커지고, y 좌표는 위에서 아래로 갈수록 커집니다.