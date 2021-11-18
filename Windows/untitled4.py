# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class fourth(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1099, 559)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.l1 = QtGui.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(90, 20, 641, 71))
        self.l1.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.l1.setObjectName(_fromUtf8("l1"))
        self.im3 = QtGui.QLabel(self.centralwidget)
        self.im3.setGeometry(QtCore.QRect(10, 120, 801, 211))
        self.im3.setText(_fromUtf8(""))
        self.im3.setPixmap(QtGui.QPixmap(_fromUtf8("scanning-title-screen-technology-background-d-rendering-73432480.jpg")))
        self.im3.setObjectName(_fromUtf8("im3"))
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(470, 440, 112, 34))
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.im4 = QtGui.QLabel(self.centralwidget)
        self.im4.setGeometry(QtCore.QRect(820, 20, 271, 411))
        self.im4.setText(_fromUtf8(""))
        self.im4.setPixmap(QtGui.QPixmap(_fromUtf8("sit.PNG")))
        self.im4.setObjectName(_fromUtf8("im4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l1.setText(_translate("MainWindow", "Please sit still (as shown), the scan will begin in 10 seconds.", None))
        self.btn6.setText(_translate("MainWindow", "Finish", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('logonnnn.png'))
    ui = fourth()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

