# https://wikidocs.net/33768

## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('landscape.jpg')
        # 파일 이름을 입력해주고, QPixmap 객체 (pixmap)를 하나 만듭니다.

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        # 라벨을 하나 만들고, setPixmap을 이용해서 pixmap을 라벨에 표시될 이미지로 설정해줍니다.
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        # width()와 height()는 이미지의 너비, 높이를 반환합니다.
        # 너비, 높이를 표시하는 라벨 (lbl_size)를 하나 만들고,
        # setAlignment 메서드를 이용해서 가운데 정렬로 설정합니다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)
        # 수평 박스 레이아웃을 하나 만들고 라벨을 배치합니다.
        # setLayout()을 이용해서 수평 박스(hbox)를 창의 레이아웃으로 지정해줍니다.

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())