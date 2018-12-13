# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot
from paint_datas.digits_recognition import module2 as dr
import random as rm
from os import system

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 401)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 100, 221, 31))
        font = QtGui.QFont()
        font.setKerning(False)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 261, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getImage)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 20, 251, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.digitsRecognizeOnClick)
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setObjectName("image_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 70, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 300, 531, 61))
        self.pushButton_3.setStyleSheet("#pushButton_3 {\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    border-image: url(buttons/paint_datas_button1.png);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openPaintDatas)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.imageName = None
        if self.imageName == None:
            self.pushButton_2.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Открыть картинку"))
        self.pushButton_2.setText(_translate("MainWindow", "Распознать"))
        self.label.setText(_translate("MainWindow", "Прогноз от программы"))
        self.pushButton_3.setText(_translate("MainWindow", "Открыть редактор"))
        self.label_2.setText(_translate("MainWindow", "Выбранная картинка"))

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Open image",
                                                  "paint_datas/application.windows64/lib/img/", "image/x-png (*.png)", options=options)
        if fileName:
            return fileName

    def getImage(self):
        self.imageName = self.openFileDialog()
        image = QtGui.QPixmap(self.imageName).scaledToHeight(128).scaledToWidth(182)
        x, y = 50, 70
        self.image_label.setGeometry(QtCore.QRect(x, y, x + image.width(), y + image.height()))
        self.image_label.setPixmap(image)
        self.image_label.show()
        if self.imageName != None:
            self.pushButton_2.setDisabled(False)

    def digitsRecognizeOnClick(self):
        if self.imageName != None:
            dr.main(self.imageName)
        with open('data/data.txt', 'r') as f:
            text = f.read()
        f.close()
        pre = ['Наверняка это', 'Скорее всего это', '100% это', 'Это точно', 'Зуб даю, это', 'Не, ну это']
        dig_tran = {0:"ноль", 1:"один", 2:"два", 3:"три",
                    4:"четыре", 5:"пять", 6:"шесть", 7:"семь",
                    8:"восемь", 9:"девять"}
        pre_phrase = rm.choice(pre)
        self.textEdit.setText(f"{pre_phrase} {dig_tran[int(text[1])]}")

    def openPaintDatas(self):
        system("/Tensolvers/paint_datas/application.windows64/paint_datas.exe")

if __name__ == "__main__":

    import sys
    sys._excepthook = sys.excepthook

    def myExceptionHook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = myExceptionHook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

