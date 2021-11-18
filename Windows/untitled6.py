# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled6.ui'
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

class sixth(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(767, 821)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.l3 = QtGui.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(60, 110, 691, 51))
        self.l3.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.l3.setObjectName(_fromUtf8("l3"))
        self.title5 = QtGui.QLabel(self.centralwidget)
        self.title5.setGeometry(QtCore.QRect(60, 20, 681, 81))
        self.title5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title5.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";"))
        self.title5.setObjectName(_fromUtf8("title5"))
        self.title6 = QtGui.QLabel(self.centralwidget)
        self.title6.setGeometry(QtCore.QRect(310, 180, 181, 51))
        self.title6.setStyleSheet(_fromUtf8("font: 75 20pt \"Arial\";\n"
"text-decoration: underline;\n"
"\n"
"\n"
"\n"
""))
        self.title6.setObjectName(_fromUtf8("title6"))
        self.Im5 = QtGui.QLabel(self.centralwidget)
        self.Im5.setGeometry(QtCore.QRect(30, 230, 541, 541))
        self.Im5.setText(_fromUtf8(""))
        self.Im5.setPixmap(QtGui.QPixmap(_fromUtf8("anshul.PNG")))
        self.Im5.setObjectName(_fromUtf8("Im5"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 500, 112, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l3.setText(_translate("MainWindow", "The scan has been sent for printing. Please collect it from x room in y minutes", None))
        self.title5.setText(_translate("MainWindow", "Thank you, visit again!", None))
        self.title6.setText(_translate("MainWindow", "Our Team", None))
        self.pushButton.setText(_translate("MainWindow", "Finish", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('logonnnn.png'))
    ui = sixth()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

