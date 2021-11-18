# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untitled3 import third
#from GUI import first

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

class second(object):
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()

    def open3(self, x):
        self.window = QtGui.QMainWindow()
        self.ui = third()
        self.ui.setupUi(self.window)
        x.hide()
        self.window.show()
    
    def open3n(self, x):
        x.hide()
        global MainWindow
        MainWindow.show()
        #self.window = QtGui.QMainWindow()
        #self.ui = first()
        #self.ui.first1(self.window)
        #self.window.show()
        
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(701, 608)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 0, 521, 81))
        self.label.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";\n"
"\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn2 = QtGui.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(100, 540, 121, 34))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btn3 = QtGui.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(470, 540, 112, 34))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 701, 441))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Capture.PNG")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #if self.btn2.isEnabled():
        #    print "a"
            
         #   self.hide()
         #   print "jgh"

        self.btn2.clicked.connect(lambda: self.open3(Dialog)) #lambda will avoid the evaluation of the function call
        #Dialog.hide()
        #open4n()
        self.btn3.clicked.connect(lambda: self.open3n(Dialog))
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Payment Gateway", None))
        self.btn2.setText(_translate("Dialog", "Proceed to pay", None))
        self.btn3.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    Dialog.setWindowIcon(QtGui.QIcon('logonnnn.png'))
    ui = second()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

