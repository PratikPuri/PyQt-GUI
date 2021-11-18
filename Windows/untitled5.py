# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untitled3 import third
from untitled6 import sixth

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class fifth(object):

    def open6(self, MainWindow):
       self.window = QtGui.QMainWindow()
       self.ui = sixth()
       self.ui.setupUi(self.window)
       MainWindow.hide()
       self.window.show()

    def open7(self, MainWindow):
       self.window = QtGui.QMainWindow()
       self.ui = third()
       self.ui.setupUi(self.window)
       MainWindow.hide()
       self.window.show()
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title5 = QtGui.QLabel(self.centralwidget)
        self.title5.setGeometry(QtCore.QRect(100, 20, 601, 61))
        self.title5.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";"))
        self.title5.setObjectName(_fromUtf8("title5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 391, 21))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.r1 = QtGui.QRadioButton(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(430, 160, 40, 25))
        self.r1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r1.setObjectName(_fromUtf8("r1"))
        self.r2 = QtGui.QRadioButton(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(510, 160, 41, 25))
        self.r2.setObjectName(_fromUtf8("r2"))
        self.r3 = QtGui.QRadioButton(self.centralwidget)
        self.r3.setGeometry(QtCore.QRect(750, 160, 41, 25))
        self.r3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r3.setObjectName(_fromUtf8("r3"))
        self.r4 = QtGui.QRadioButton(self.centralwidget)
        self.r4.setGeometry(QtCore.QRect(670, 160, 41, 25))
        self.r4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r4.setObjectName(_fromUtf8("r4"))
        self.r5 = QtGui.QRadioButton(self.centralwidget)
        self.r5.setGeometry(QtCore.QRect(590, 160, 41, 25))
        self.r5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r5.setObjectName(_fromUtf8("r5"))
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(240, 240, 341, 71))
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(80, 370, 231, 71))
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(510, 370, 231, 71))
        self.btn9.setObjectName(_fromUtf8("btn9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.btn7.clicked.connect(lambda: self.open6(MainWindow))
        self.btn8.clicked.connect(lambda: self.open7(MainWindow))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.title5.setText(_translate("MainWindow", "Feedback and print", None))
        self.label_2.setText(_translate("MainWindow", "Please rate the quality of your scan:", None))
        self.r1.setText(_translate("MainWindow", "1", None))
        self.r2.setText(_translate("MainWindow", "2", None))
        self.r3.setText(_translate("MainWindow", "5", None))
        self.r4.setText(_translate("MainWindow", "4", None))
        self.r5.setText(_translate("MainWindow", "3", None))
        self.btn7.setText(_translate("MainWindow", "Click here to get a 3D print of your scan", None))
        self.btn8.setText(_translate("MainWindow", "Not satisfactory : Re-scan", None))
        self.btn9.setText(_translate("MainWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('logonnnn.png'))
    ui = fifth()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

