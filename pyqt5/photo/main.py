import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import os




form_class = uic.loadUiType("form.ui")[0]

fname = r'C:\Users\82104\Desktop\lena.jpg'
img = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg', cv2.IMREAD_COLOR)
# kernel = np.ones((5,5),np.float32)/25 블러
# dst = cv2.filter2D(img, -1, kernel)
# cv2.imshow('Result', dst)

# imgGray = cv2.imread(img, cv2.IMREAD_GRAYSCALE) #그레이스케일
# dst = cv2.bitwise_not(img)

# kernel_sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])  # sharpening
# output_1 = cv2.filter2D(img,-1,kernel_sharpen_1)
# cv2.imshow('Sharpening',output_1)
# cv2.waitKey()


class MyWindow(QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show()



    def initUI(self):
        self.btn.clicked.connect(self.showDialog)
        self.setWindowTitle('File Dialog')
        self.radioBtn1.clicked.connect(self.dix)
        self.radioBtn2.clicked.connect(self.dix)
        #self.RB3.clicked.connect(self.dix)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        print(fname[0])
        if fname[0]:
            pixmap = QPixmap(fname[0])
            pixmap = pixmap.scaledToWidth(130) #re size
        # 파일 이름을 입력해주고, QPixmap 객체 (pixmap)를 하나 만듭니다.

        self.lbl.setPixmap(pixmap)
        print(pixmap)

    def LoadImage(self):
        self.orgImg = cv2.imread(self.fname)

    def dix(self):
        if (self.radioBtn1.isChecked()):
            print("radioBtn1")
            # cv2.imshow("test",self.orgImg)
            blur = cv2.blur(self.orgImg, (5, 5))
            cv2.imshow('blur',blur)
            cv2.waitKey()
            blurRGB = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
            qimg = QImage(blurRGB.data, blurRGB.shape[1], blurRGB.shape[0], QImage.Format_RGB888)
            pixmap01 = QPixmap.fromImage(qimg)
            self.lbl2.setPixmap(pixmap01)

        #
        #    f = open(fname[0], 'r')
    # def radioBtn(self):
    #     if self.radioBtn1.isChecked(): # 블러
    #         kernel = np.ones((5, 5), np. float32)/25
    #         blur = cv2.imread(r'C:\Users\82104\Desktop\lena.jpg')
    #         self.lbl2.
    #         #cv2.imshow('blur')







if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


