## Ex 5-2. QLabel.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)
        # QLabel 위젯을 하나 만들었습니다. 생성자에 라벨 텍스트와 부모 위젯을 입력해줍니다.
        # setAlignment() 메서드로 라벨의 배치를 설정할 수 있습니다.
        # Qt.AlignCenter로 설정해주면 수평, 수직 방향 모두 가운데 위치하게 됩니다.

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)
        # 라벨에 사용될 폰트를 하나 만들었습니다.
        # setPointSize() 메서드로 폰트의 크기를 설정해줍니다.

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        # 두번째 라벨에 설정할 폰트를 하나 만들고, setFamily()
        # 메서드로 폰트의 종류를 'Times New Roman'으로 설정해줍니다.
        # setBold(True)로 폰트를 진하게 설정합니다.
        # 이번에는 폰트의 크기를 설정하지 않았기 때문에 디폴트 크기인 13으로 설정됩니다.

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())