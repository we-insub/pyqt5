import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import *
from PyQt5 import uic, QtCore
import cv2
import numpy as np

form_class = uic.loadUiType("form3.ui")[0]

class MyApp(QWidget,form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.show()

    def initUI(self):

        self.BTN1.clicked.connect(self.showDialog)
        self.RB1.clicked.connect(self.dix)
        self.RB2.clicked.connect(self.dix)
        self.RB3.clicked.connect(self.dix)

        self.CHB1.stateChanged.connect(self.Check)
        self.CHB2.stateChanged.connect(self.Check)

    def showDialog(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file', './')
        print(self.fname)
        self.showOrgImage()
        self.loadImage()

    def showOrgImage(self):
        self.pixmap = QPixmap(self.fname)
        self.pixmap1 = self.pixmap.scaled(201,181)
        self.LE.setPixmap(self.pixmap1)

    def loadImage(self):
        # Channel order : BGR
        self.orgImg = cv2.imread(self.fname)

    def dix(self):
        if (self.RB1.isChecked()):
            print("RB1")
            cv2.imshow("test",self.orgImg)
            blur = cv2.blur(self.orgImg, (5, 5))
            #cv2.waitKey()
            blurRGB = cv2.cvtColor(blur,cv2.COLOR_BGR2RGB)
            qimg = QImage(blurRGB.data,blurRGB.shape[1], blurRGB.shape[0], QImage.Format_RGB888)
            pixmap01 = QPixmap.fromImage(qimg)
            self.LE2.setPixmap(pixmap01)

        if (self.RB2.isChecked()):
            print("RB2")

            cv2.imshow("test", self.orgImg)

            sharpen_2 = np.array([[1,1,1],[1,-7,1],[1,1,1]])
            output_2 = cv2.filter2D(self.orgImg,-1,sharpen_2)

            cv2.imshow('Sharpening', output_2)
            # cv2.imshow('Excessive Sharpening',output_2)
            # cv2.imshow('Edge Enhancement',output_3)


    def Check(self):
        CBox = self.sender()
        if self.gray == CBox:
            print("gray")
            self.grayB = self.gray.isChecked()
            if self.grayB == True:
                grayS = cv2.cvtColor(self.orgImg, cv2.COLOR_BGR2GRAY)  # 이미지 색깔 변경하기
                qimg = QImage(grayS.data, grayS.shape[1], grayS.shape[0], QImage.Format_RGB888)
                qpix_des = QPixmap.fromImage(qimg)

                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(qpix_des)

            if self.grayB == False:
                self.result_imgShow(self.src_pixmap)

        if self.invert == CBox:
            print("invert")
            self.invertB = self.invert.isChecked()
            if self.invertB == True:
                dst_invert = cv2.bitwise_not(self.orgImg)
                qimg = QImage(dst_invert.data, dst_invert.shape[1], dst_invert.shape[0], QImage.Format_RGB888)
                qpix_des = QPixmap.fromImage(qimg)

                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(qpix_des)

            if self.invertB == False:
                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(self.src_pixmap)

    # def Check(self):
    #     if (self.CHB2.isChecked()):
    #         print('CHB2')
    #         src_bgr = cv2.imread("src.jpg", self.orgImg)
    #         invert_img = cv2.bitwise_not(self.orgImg)
    #         cv2.imshow("test", invert_img)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())