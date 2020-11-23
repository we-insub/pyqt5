## Ex 5-15. QDoubleSpinBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        # QDoubleSpinBox 객체 (self.dspinbox)를 하나 만듭니다.
        #
        # setRange() 메서드를 이용해서 선택 범위를 제한할 수 있습니다.
        # 최소값은 0.0, 최대값은 99.99가 디폴트입니다.
        #
        # setSingleStep() 메서드를 이용해서 한 스텝을 0.5로 설정해줍니다.
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        # setPrefix()를 이용해서, 숫자 앞에 올 문자를 설정할 수 있습니다.
        # setSuffix()는 숫자 뒤에 문자가 오도록 합니다.
        #
        # setDecimals()를 이용해서 소수점 아래 표시될 자리수를 정해줍니다.
        self.lbl2 = QLabel('$ 0.0')

        self.dspinbox.valueChanged.connect(self.value_changed)
        # 더블 스핀 박스 위젯의 값이 변경될 때 발생하는 시그널
        # (valueChanged)을 self.value_changed 메서드에 연결합니다.

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)
        # 수직 박스 레이아웃을 이용해서 라벨 두 개와 스핀 박스 위젯을
        # 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.

        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText('$ ' + str(self.dspinbox.value()))
        # 더블 스핀 박스의 값이 변경될 때,
        # self.lbl2의 텍스트를 더블 스핀 박스의 값
        # (self.dspinbox.value())으로 설정하도록 합니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())