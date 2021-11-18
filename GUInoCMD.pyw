from PyQt4 import QtCore, QtGui, QtWebKit 
from PyQt4.QtCore import QTimer

import pyautogui
from PIL import Image
import os
import time

f = open("feedback.txt", "a")
timer = QtCore.QTimer()

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

class first(object): 

    # Home Page
    
    def open2(self, x):
        self.window = QtGui.QDialog()
        self.setupUi(self.window)
        x.hide()
        self.window.show()
        
    def first1(self, MainWindow): 
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(917, 695)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Im1 = QtGui.QLabel(self.centralwidget)
        self.Im1.setGeometry(QtCore.QRect(30, 90, 851, 481))
        self.Im1.setText(_fromUtf8(""))
        self.Im1.setPixmap(QtGui.QPixmap(_fromUtf8("References/12.jpg")))
        self.Im1.setObjectName(_fromUtf8("Im1"))
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(410, 590, 112, 34))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.title1 = QtGui.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(10, 10, 901, 71))
        self.title1.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";"))
        self.title1.setObjectName(_fromUtf8("label1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))
        
        self.btn1.clicked.connect(lambda: self.open2(MainWindow)) #lambda will avoid the evaluation of the function call

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn1.setText(_translate("MainWindow", "Enter", None))
        self.title1.setText(_translate("MainWindow", "Welcome to robo 3d scanner", None))

    # Payment Gateway

    def open3(self, x):
        self.window = QtGui.QMainWindow()
        self.ui = first()
        self.ui.setupUi2(self.window)
        x.close()
        self.window.show()
    
    def open3n(self, x):
        x.close()
        global MainWindow
        MainWindow.show()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(701, 608)
        self.title2 = QtGui.QLabel(Dialog)
        self.title2.setGeometry(QtCore.QRect(80, 0, 521, 81))
        self.title2.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";\n"
"\n"
""))
        self.title2.setObjectName(_fromUtf8("title2"))
        self.btn2 = QtGui.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(100, 540, 121, 34))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btn3 = QtGui.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(470, 540, 112, 34))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.Im2 = QtGui.QLabel(Dialog)
        self.Im2.setGeometry(QtCore.QRect(0, 80, 701, 441))
        self.Im2.setText(_fromUtf8(""))
        self.Im2.setPixmap(QtGui.QPixmap(_fromUtf8("References/Capture.PNG")))
        self.Im2.setObjectName(_fromUtf8("label_2"))
        
        self.retranslateUi1(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.setWindowIcon(QtGui.QIcon('References/logo.png'))

        self.btn2.clicked.connect(lambda: self.open3(Dialog)) #lambda will avoid the evaluation of the function call
        self.btn3.clicked.connect(lambda: self.open3n(Dialog))
        
    def retranslateUi1(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.title2.setText(_translate("Dialog", "Payment Gateway", None))
        self.btn2.setText(_translate("Dialog", "Proceed to pay", None))
        self.btn3.setText(_translate("Dialog", "Cancel", None))


    # Instructions


    def checkbox(self, otherWindow):
        if self.check1.isChecked():
            self.open4(otherWindow)
        else:
            pass
            
    def open4(self, otherWindow):
        self.window = QtGui.QMainWindow()
        self.ui = first()
        self.ui.setupUi5(self.window)
        otherWindow.close()
        self.window.show()
        QTimer.singleShot(10000, lambda: self.open41(self.window))

    def open41(self, a):
        a.close()
        self.x()
        
    def open4n(self, x):
        x.close()
        global MainWindow
        MainWindow.show()
        
    def setupUi2(self, otherWindow):
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

        self.retranslateUi2(otherWindow)
        QtCore.QMetaObject.connectSlotsByName(otherWindow)

        otherWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))

        self.btn4.clicked.connect(lambda: self.checkbox(otherWindow))

        self.btn5.clicked.connect(lambda: self.open4n(otherWindow))

    def retranslateUi2(self, otherWindow):
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

    # Scanning start    

    def setupUi5(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1099, 559)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title4 = QtGui.QLabel(self.centralwidget)
        self.title4.setGeometry(QtCore.QRect(90, 20, 641, 71))
        self.title4.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.title4.setObjectName(_fromUtf8("title4"))
        self.Im3 = QtGui.QLabel(self.centralwidget)
        self.Im3.setGeometry(QtCore.QRect(10, 120, 801, 211))
        self.Im3.setText(_fromUtf8(""))
        self.Im3.setPixmap(QtGui.QPixmap(_fromUtf8("References/scanning-title-screen-technology-background-d-rendering-73432480.jpg")))
        self.Im3.setObjectName(_fromUtf8("Im3"))
        self.Im4 = QtGui.QLabel(self.centralwidget)
        self.Im4.setGeometry(QtCore.QRect(820, 20, 271, 411))
        self.Im4.setText(_fromUtf8(""))
        self.Im4.setPixmap(QtGui.QPixmap(_fromUtf8("References/sit.PNG")))
        self.Im4.setObjectName(_fromUtf8("Im4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi5(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        timer = QTimer(MainWindow)
        timer.setInterval(10)
        timer.start()

        MainWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))

    def retranslateUi5(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.title4.setText(_translate("MainWindow", "Please sit still (as shown), the scan will begin in 10 seconds.", None))
        
    # Automation

    def open5(self):
        self.window = QtGui.QMainWindow()
        self.ui = first()
        self.ui.setupUi3(self.window)
        self.window.show()

    def x(self):

        pyautogui.keyDown('winleft');pyautogui.press('d'); pyautogui.keyUp('winleft');

        time.sleep(5)
        
        x=pyautogui.locateOnScreen('References/g.png')
        x1=pyautogui.center(x)
        pyautogui.click(x1)
        time.sleep(10)

        z=pyautogui.locateOnScreen('References/max.png')
        z1=pyautogui.center(z)
        pyautogui.click(z1)
        time.sleep(5)

        def func(y):
            x = pyautogui.screenshot()
            return pyautogui.locate(y,x)    

        a1 = func('References/start.png')
        if a1==None:
            a1 = func('References/start1.png')
        a2 = pyautogui.center(a1)
        pyautogui.click(a2)
        pyautogui.click(a2)
        time.sleep(4)

        b1 = func('References/startrec.png')
        if b1==None:
            b1 = func('References/startrec1.png')
        b2 = pyautogui.center(b1)
        pyautogui.click(b2)

        time.sleep(240)

        pyautogui.click(b2)

        time.sleep(180)

        e1 = func('References/process.png')
        if e1==None:
            e1 = func('References/processb.png')
        e2 = pyautogui.center(e1)
        pyautogui.click(e2)

        time.sleep(2)

        f1 = func('References/fill1.png')
        if f1==None:
            f1 = func('References/fill2.png')
        f2 = pyautogui.center(f1)
        pyautogui.click(f2)

        time.sleep(2)

        g1 = func('References/closed.png')
        if g1==None:
            g1 = func('References/closedb.png')
        g2 = pyautogui.center(g1)
        pyautogui.click(g2)

        time.sleep(2)

        n1 = func('References/run.png')
        if n1==None:
            n1 = func('References/runb.png')
        n2 = pyautogui.center(n1)
        pyautogui.click(n2)
        pyautogui.click(n2)

        time.sleep(20)

        i1 = func('References/watertight.png')
        if i1==None:
            i1 = func('References/watertightb.png')
        i2 = pyautogui.center(i1)
        pyautogui.click(i2)

        time.sleep(2)

        o1 = func('References/run1.png')
        if o1==None:
            o1 = func('References/runb1.png')
        o2 = pyautogui.center(o1)
        pyautogui.click(o2)
        pyautogui.click(o2)

        time.sleep(20)

        p1 = func('References/share.png')
        if p1==None:
            p1 = func('References/shareb.png')
        p2 = pyautogui.center(p1)
        pyautogui.click(p2)

        time.sleep(2)

        k1 = func('References/export.png')
        if k1==None:
            k1 = func('References/exportb.png')
        k2 = pyautogui.center(k1)
        pyautogui.click(k2)

        time.sleep(2)

        l1 = func('References/stl.png')
        if l1==None:
            l1 = func('References/stlb.png')
        l2 = pyautogui.center(l1)
        pyautogui.click(l2)
        pyautogui.click(l2)

        time.sleep(2)

        m1 = func('References/export1.png')
        if m1==None:
            m1 = func('References/export1b.png')
        m2 = pyautogui.center(m1)
        pyautogui.click(m2)
        pyautogui.click(m2)
        
        self.open5()

    # Feedback and print

    def open6(self, MainWindow):
        self.window = QtGui.QMainWindow()
        self.ui = first()
        self.ui.setupUi4(self.window)
        MainWindow.hide()
        self.window.show()

    def open7(self, MainWindow):
        self.window = QtGui.QMainWindow()
        self.ui = first()
        self.ui.setupUi2(self.window)
        MainWindow.hide()
        self.window.show()

    def open8(self, x):
        x.close()
        global MainWindow
        MainWindow.show()

    def open11(self):
        global f
        f = open("feedback.txt", "a")
        if self.r1.isChecked():
            f.write("1 \n")
        elif self.r2.isChecked():
            f.write("2 \n")
        elif self.r3.isChecked():
            f.write("3 \n")    
        elif self.r4.isChecked():
            f.write("4 \n")
        elif self.r5.isChecked():
            f.write("5 \n")
        f.close()
            
    def setupUi3(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title5 = QtGui.QLabel(self.centralwidget)
        self.title5.setGeometry(QtCore.QRect(100, 20, 601, 61))
        self.title5.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";"))
        self.title5.setObjectName(_fromUtf8("title5"))
        self.l1 = QtGui.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(20, 160, 391, 21))
        self.l1.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.l1.setObjectName(_fromUtf8("l1"))
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
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(240, 240, 341, 71))
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(80, 370, 231, 71))
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(510, 370, 231, 71))
        self.btn8.setObjectName(_fromUtf8("btn8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.btn6.clicked.connect(lambda: self.open6(MainWindow))
        self.btn7.clicked.connect(lambda: self.open7(MainWindow))
        self.btn8.clicked.connect(lambda: self.open8(MainWindow))
        self.r1.clicked.connect(self.open11)
        self.r2.clicked.connect(self.open11)
        self.r3.clicked.connect(self.open11)
        self.r4.clicked.connect(self.open11)
        self.r5.clicked.connect(self.open11)

        self.retranslateUi3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))

    def retranslateUi3(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.title5.setText(_translate("MainWindow", "Feedback and print", None))
        self.l1.setText(_translate("MainWindow", "Please rate the quality of your scan:", None))
        self.r1.setText(_translate("MainWindow", "1", None))
        self.r2.setText(_translate("MainWindow", "2", None))
        self.r3.setText(_translate("MainWindow", "3", None))
        self.r4.setText(_translate("MainWindow", "4", None))
        self.r5.setText(_translate("MainWindow", "5", None))
        self.btn6.setText(_translate("MainWindow", "Click here to get a 3D print of your scan", None))
        self.btn7.setText(_translate("MainWindow", "Not satisfactory : Re-scan", None))
        self.btn8.setText(_translate("MainWindow", "Quit", None))

    #Thank you page

    def open9(self, x):
        x.close()
        global MainWindow
        MainWindow.show()

    def setupUi4(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(767, 821)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.l2 = QtGui.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(60, 110, 691, 51))
        self.l2.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.l2.setObjectName(_fromUtf8("l2"))
        self.title6 = QtGui.QLabel(self.centralwidget)
        self.title6.setGeometry(QtCore.QRect(60, 20, 681, 81))
        self.title6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title6.setStyleSheet(_fromUtf8("font: 75 28pt \"BankGothic Lt BT\";"))
        self.title6.setObjectName(_fromUtf8("title6"))
        self.title7 = QtGui.QLabel(self.centralwidget)
        self.title7.setGeometry(QtCore.QRect(310, 180, 181, 51))
        self.title7.setStyleSheet(_fromUtf8("font: 75 20pt \"Arial\";\n"
"text-decoration: underline;\n"
"\n"
"\n"
"\n"
""))
        self.title7.setObjectName(_fromUtf8("title7"))
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(610, 500, 112, 34))
        self.btn9.setObjectName(_fromUtf8("btn9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi4(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))

        self.btn9.clicked.connect(lambda: self.open9(MainWindow))

    def retranslateUi4(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l2.setText(_translate("MainWindow", "The scan has been sent for printing. Please collect it from x room in y minutes", None))
        self.title6.setText(_translate("MainWindow", "Thank you, visit again!", None))
        self.title7.setText(_translate("MainWindow", "Our Team", None))
        self.btn9.setText(_translate("MainWindow", "Finish", None))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = first()
    ui.first1(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon('References/logo.png'))
    MainWindow.show()
    sys.exit(app.exec_())
