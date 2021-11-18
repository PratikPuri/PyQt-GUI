# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untitled4 import fourth
from a import func, x

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

class third(object):
    
    def open4(self, otherWindow):
       #self.window = QtGui.QMainWindow()
       #self.ui = fourth()
       #self.ui.setupUi(self.window)
       otherWindow.hide()
       #self.window.show()
       x()
            
    def setupUi(self, otherWindow):
        otherWindow.setObjectName(_fromUtf8("otherWindow"))
        otherWindow.resize(805, 578)
        self.centralwidget = QtGui.QWidget(otherWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title3 = QtGui.QLabel(self.centralwidget)
        self.title3.setGeometry(QtCore.QRect(50, 20, 701, 51))
        self.title3.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";\n"
""))
        self.title3.setObjectName(_fromUtf8("title3"))
        self.text1 = QtGui.QPlainTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(26, 90, 751, 281))
        self.text1.setObjectName(_fromUtf8("text1"))
        self.check1 = QtGui.QCheckBox(self.centralwidget)
        self.check1.setGeometry(QtCore.QRect(30, 400, 601, 41))
        self.check1.setObjectName(_fromUtf8("check1"))
        self.btn4 = QtGui.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(170, 470, 112, 34))
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.btn5 = QtGui.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(510, 470, 112, 34))
        self.btn5.setObjectName(_fromUtf8("btn5"))
        otherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(otherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        otherWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(otherWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        otherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherWindow)
        QtCore.QMetaObject.connectSlotsByName(otherWindow)

        self.btn4.clicked.connect(lambda: self.open4(otherWindow))

    def retranslateUi(self, otherWindow):
        otherWindow.setWindowTitle(_translate("otherWindow", "MainWindow", None))
        self.title3.setText(_translate("otherWindow", "Important instructions", None))
        self.text1.setPlainText(_translate("otherWindow", "1)  The scanning process will begin 10 seconds after you press \"proceed\".\n"
"\n"
"\n"
"2) Please sit still facing forward during the scanning process to obtain a good quality scan.\n"
"\n"
"3)The scanning process would take approximately 4 minutes.\n"
"\n"
"\n"
"4) At the end of the scan, a 3D model of your scan will be displayed. In case you are not satisfied with the scan you can restart the scan.\n"
"\n"
"\n"
"5) Once a proper scan has been obtained you would be asked for payment for the 3D print if needed. You could either proceed to pay or quit at the moment.", None))
        self.check1.setText(_translate("otherWindow", "I have read all the instructions carefully.", None))
        self.btn4.setText(_translate("otherWindow", "Proceed", None))
        self.btn5.setText(_translate("otherWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    otherWindow = QtGui.QMainWindow()
    otherWindow.setWindowIcon(QtGui.QIcon('logonnnn.png'))
    ui = third()
    ui.setupUi(otherWindow)
    otherWindow.show()
    sys.exit(app.exec_())

