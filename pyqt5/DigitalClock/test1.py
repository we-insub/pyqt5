# # 'C:\Users\82104\Desktop\캡처.png'
# # import cv2
# # fname = r'C:\Users\82104\Desktop\lena.jpg'
# # img = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg', cv2.IMREAD_COLOR)
# # print(img.shape)
# # cv2.imshow('lena', img)
# # Imige show()
#
#
# # import cv2
# #
# # imageFile = r'C:\Users\82104\Desktop\lena.jpg'
# # img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
# # img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE
# # cv2.imshow('Lena color',img)
# # cv2.imshow('Lena grayscale',img2)
# #
# # cv2.waitKey()
# # cv2.destroyAllWindows()
#
#
#
# # GRAY_SCALE
# # import cv2
# # from   matplotlib import pyplot as plt
# #
# # imageFile = r'C:\Users\82104\Desktop\lena.jpg'
# # imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
# #
# # plt.figure(figsize=(6,6))
# # plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
# # plt.imshow(imgGray, cmap = 'gray')
# # ##plt.axis('tight')
# # plt.axis('off')
# # #plt.savefig('./data/0205.png')
# # plt.show()
# #
# # Blur
# # import numpy as np
# # import cv2
# #
# # fname = r'C:\Users\82104\Desktop\lena.jpg'
# # img = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg', cv2.IMREAD_COLOR)
# # kernel = np.ones((5,5),np.float32)/25
# # dst = cv2.filter2D(img, -1, kernel)
# #
# #
# # cv2.imshow('Original', img)
# # cv2.imshow('Result', dst)
# #
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# #
# # # #invert
# # import cv2
# #
# # imageFile = r'C:\Users\82104\Desktop\lena.jpg'
# # img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
# # dst = cv2.bitwise_not(img)
# #
# # cv2.imshow("img", img)
# # cv2.imshow("dst", dst)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# #
# # import cv2
# # import numpy as np
# # imageFile = r'C:\Users\82104\Desktop\lena.jpg'
# # img  = cv2.imread(imageFile)
# # #cv2.imshow('Original',img)
# #
# kernel_sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]) #정규화를 하지 않은 이유는 모든 값을 다 더하면 1이되기때문에 1로 나눈것과 같은 효과
# #applying different kernels to the input image
# output_1 = cv2.filter2D(img,-1,kernel_sharpen_1)
#
# cv2.imshow('Sharpening',output_1)
# #cv2.imshow('Excessive Sharpening',output_2)
# #cv2.imshow('Edge Enhancement',output_3)
# cv2.waitKey()
#
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QPixmap
# from PyQt5 import QtCore, QtGui, QtWidgets
# import numpy as np
# import cv2
# import os
#
# # form_class = uic.loadUiType("form.ui")[0]
# import cv2
# from PyQt5 import QtWidgets
# from PyQt5 import QtGui
#
# app = QApplication(sys.argv)
# lbl2 = QtWidgets.QLabel()
#
# fname = r'C:\Users\82104\Desktop\lena.jpg'
# img = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg', cv2.IMREAD_COLOR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# h,w,c = img.shape
# qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
# pixmap = QtGui.QPixmap.fromImage(qImg)
# lab.setPixmap(pixmap)
# lbl2.resize(pixmap.width(), pixmap.height())
# lbl2.show()
# #
# # app.exec_()
# #
# # import sys
# # from PyQt5.QtWidgets import *
# # from PyQt5 import uic
# # from PyQt5.QtGui import QIcon
# # from PyQt5.QtGui import QPixmap
# # from PyQt5 import QtCore, QtGui, QtWidgets
# # import numpy as np
# # import cv2
# # import os
# #
# # form_class = uic.loadUiType("form.ui")[0]
# # class MyWindow(QMainWindow, form_class):
# #
# #     def __init__(self):
# #         super().__init__()
# #         self.setupUi(self)
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.btn.clicked.connect(self.showDialog)
# #         self.setWindowTitle('File Dialog')
# #         self.show()
# #
# #     def showDialog(self):
# #         fname = QFileDialog.getOpenFileName(self, 'Open file', './')
# #         # QFileDialog를 띄우고, getOpenFileName() 메서드를 사용해서 파일을 선택합니다.
# #         #
# #         # 세 번째 매개변수를 통해 기본 경로를 설정할 수 있습니다.
# #         # 또한 기본적으로 모든 파일( * )을 열도록 되어있습니다.
# #
# #         print(fname[0])
# #         if fname[0]:
# #             pixmap = QPixmap(fname[0])
# #             pixmap = pixmap.scaledToWidth(130) #re size
# #         # 파일 이름을 입력해주고, QPixmap 객체 (pixmap)를 하나 만듭니다.
# #
# #         self.lbl.setPixmap(pixmap)
# #         print(pixmap)
# #
# #
# # app = QApplication(sys.argv)
# # lbl2 = QtWidgets.QLabel()
# #
# # fname = r'C:\Users\82104\Desktop\lena.jpg'
# # img = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg', cv2.IMREAD_COLOR)
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # h,w,c = img.shape
# # qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
# # pixmap = QtGui.QPixmap.fromImage(qImg)
# # lbl2.setPixmap(pixmap)
# # lbl2.resize(pixmap.width(), pixmap.height())
# # lbl2.show()
# #
# # app.exec_()
#
# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel
# # from PyQt5.QtGui import QIcon, QPixmap, QImage
# # from PyQt5.QtCore import *
# # from PyQt5 import uic, QtCore
# # import cv2
# # import numpy as np
# # from matplotlib import pyplot as plt
# #
# # form_class = uic.loadUiType("form3.ui")[0]
# #
# # class MyApp(QWidget,form_class):
# #
# #     def __init__(self):
# #         super().__init__()
# #         self.setupUi(self)
# #         self.initUI()
# #
# #         self.show()
# #
# #     def initUI(self):
# #
# #         #self.textEdit = QTextEdit()
# #         #self.setCentralWidget(self.textEdit)
# #         #self.statusBar()
# #
# #         #openFile = QAction(QIcon('open.png'), 'Open', self)
# #         #openFile.setShortcut('Ctrl+O')
# #         #openFile.setStatusTip('Open New File')
# #         self.BTN1.clicked.connect(self.showDialog)
# #         self.RB1.clicked.connect(self.dix)
# #         self.RB2.clicked.connect(self.dix)
# #         self.RB3.clicked.connect(self.dix)
# #
# #     def showDialog(self):
# #         self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file', './')
# #         self.showOrgImage()
# #         self.loadImage()
# #
# #     def showOrgImage(self):
# #         self.pixmap = QPixmap(self.fname)
# #         self.pixmap1 = self.pixmap.scaled(201,181)
# #         self.LE.setPixmap(self.pixmap1)
# #
# #     def loadImage(self):
# #         # Channel order : BGR
# #         self.orgImg = cv2.imread(self.fname)
# #
# #     def dix(self):
# #         if (self.RB1.isChecked()):
# #             print("RB1")
# #             #cv2.imshow("test",self.orgImg)
# #             blur = cv2.blur(self.orgImg, (5, 5))
# #             blurRGB = cv2.cvtColor(blur,cv2.COLOR_BGR2RGB)
# #             qimg = QImage(blurRGB.data,blurRGB.shape[1], blurRGB.shape[0], QImage.Format_RGB888)
# #             pixmap01 = QPixmap.fromImage(qimg)
# #             self.LE2.setPixmap(pixmap01)
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = MyApp()
# #     sys.exit(app.exec_())

import te