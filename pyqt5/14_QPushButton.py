# # https://wikidocs.net/21934
#
# # 푸시 버튼(push button) 또는 명령 버튼(command button)은 사용자가
# # 프로그램에 명령을 내려서 어떤 동작을 하도록 할 때 사용되는 버튼이며,
# # GUI 프로그래밍에서 가장 흔하게 사용되고 중요한 위젯입니다.
# # setCheckable()	True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
# # toggle()	상태를 바꿉니다.
# # setIcon()	버튼의 아이콘을 설정합니다.
# # setEnabled()	False 설정 시, 버튼을 사용할 수 없습니다.
# # isChecked()	버튼의 선택 여부를 반환합니다.
# # setText()	버튼에 표시될 텍스트를 설정합니다.
# # text()	버튼에 표시된 텍스트를 반환합니다.
#
# # 시그널	설명
# # clicked()	버튼을 클릭할 때 발생합니다.
# # pressed()	버튼이 눌렸을 때 발생합니다.
# # released()	버튼을 눌렀다 뗄 때 발생합니다.
# # toggled()	버튼의 상태가 바뀔 때 발생합니다.
#
# ## Ex 5-1. QPushButton.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):  # 객채가 생성되어지고, 그 순간에 한번만 호출되고 창 띄우고 끝
#         self.btn1 = QPushButton('&Power on', self)  # 버튼 Power on 이 만들어짐
#         self.btn1.setCheckable(True)  # 버튼을 한번 눌렀을때 눌렸는지 확인
#         self.btn1.toggle()  # 한번누르면 체크된상태에서 눌려져있다.
#         self.btn1.clicked.connect(self.btn1.Toggle())
#         # 버튼이 눌렸을때 함수가 실행되라
#         # intui 함수를빠저나가면 하용할수없다.
#         # 버튼 1이 클릭 되었을때 이 함 수로 연결된다.
#         '''
#         btn1 = QPushButton('&Power on', self)  #
#         btn1.setCheckable(True)  #
#         btn1.toggle()  # 이렇게 하면 파워 온으로 창이 뜬다, 하지만 버튼이 눌렸을때 값이바뀌고싶다.
#         # 즉 어떤 함수를 추가해라
#         '''
#         # btn1 = QPushButton('&Button1', self) #버튼1만들어짐
#         # btn1.setCheckable(True) # 버튼을 한번 눌렀을때 눌렸는지 확인
#         # btn1.toggle() # 한번누르면 체크된상태에서 눌려져있다.
#         # QPushButton 클래스로 푸시 버튼을 하나 만듭니다.
#         # 첫 번째 파라미터로는 버튼에 나타날 텍스트,
#         # 두 번째는 버튼이 속할 부모 클래스를 지정해줍니다.
#         # 버튼에 단축키(shortcut)를 지정하고 싶으면 아래와 같이
#         # 해당 문자 앞에 ampersand('&')를 넣어주면 됩니다.
#         # 이 버튼의 단축키는 'Alt+b'가 됩니다.
#         # setCheckable()을 True로 설정해주면,
#         # 선택되거나 선택되지 않은 상태를 유지할 수 있게 됩니다.
#         # toggle() 메서드를 호출하면 버튼의 상태가 바뀌게 됩니다.
#         # 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있습니다.
#
#
#         self.btn2 = QPushButton(self) #버튼위에 무엇을 새길지 선언을 하지 않았다.
#         self.btn2.setText('Button&2')  # settext를 이용해서 버튼위에 문자를 새길수 있다.
#         # setText() 메서드로도 버튼에 표시될 텍스트를 지정할 수 있습니다.
#         # 또한 이 버튼의 단축키는 'Alt+2'가 됩니다
#
#         self.btn3 = QPushButton('Button3', self)
#         self.btn3.setEnabled(False)
#         # setenabled 를 누르면 버튼이 비활성화 된다.
#         # setEnabled()를 False로 설정하면, 버튼을 사용할 수 없게 됩니다.
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.btn1)
#         vbox.addWidget(self.btn2)
#         vbox.addWidget(self.btn3)
#
#         self.setLayout(vbox)
#         self.setWindowTitle('QPushButton')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#     def btnToggle(self):
#         #btn1 이라하면 이닛 안에서만 사용할수 있는 유아이 이기 떄문에 btn을 사용하고싶ㄷ면
#         #self 를붙여라
#         # self. 를 붙이면 전역변수처럼 사용할수 있다.
#         if self.btn1.setEnabled():
#             self.btn1.setText('Power Off')
#             # 버튼이 눌렸을때 글씨가 커지거나 스타일을 변경하고싶다면 set Style 로만든다
#
#         else:
#             self.btn1.setText('Power On')
#
#
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MyApp()
#    sys.exit(app.exec_())
#


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('&Button1', self)
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.btnToggle)

        self.btn2 = QPushButton(self)
        self.btn2.setText('Button&2')

        self.btn3 = QPushButton('Button3', self)
        self.btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btnToggle(self):
        if self.btn1.isChecked():
            self.btn1.setText('Power OFF')
        else:
            self.btn1.setText('Power ON')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())