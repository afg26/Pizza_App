from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from payment import Ui_payment_window

class Ui_simple_pizza_window(object):

    def open_payment(self):
        self.payment = QtWidgets.QMainWindow()
        self.payment_ui = Ui_payment_window()
        self.payment_ui.setupUi(self.payment)
        self.payment.show()

    def setupUi(self, simple_pizza_window):
        simple_pizza_window.setObjectName("simple_pizza_window")
        simple_pizza_window.resize(612, 613)
        self.centralwidget = QtWidgets.QWidget(simple_pizza_window)
        self.centralwidget.setObjectName("centralwidget")
        self.button06 = QtWidgets.QPushButton(self.centralwidget , clicked= lambda : self.open_payment())
        self.button06.setGeometry(QtCore.QRect(390, 550, 211, 23))
        self.button06.setObjectName("button06")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 591, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\image03.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 500, 161, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.r_button03 = QtWidgets.QRadioButton(self.frame)
        self.r_button03.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.r_button03.setObjectName("r_button03")
        self.r_button01 = QtWidgets.QRadioButton(self.frame)
        self.r_button01.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.r_button01.setObjectName("r_button01")
        self.r_button02 = QtWidgets.QRadioButton(self.frame)
        self.r_button02.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.r_button02.setObjectName("r_button02")
        self.label03 = QtWidgets.QLabel(self.centralwidget)
        self.label03.setGeometry(QtCore.QRect(10, 480, 161, 21))
        self.label03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label03.setLineWidth(8)
        self.label03.setObjectName("label03")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 500, 161, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.checkbox02 = QtWidgets.QCheckBox(self.frame_2)
        self.checkbox02.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.checkbox02.setObjectName("checkbox02")
        self.checkbox01 = QtWidgets.QCheckBox(self.frame_2)
        self.checkbox01.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.checkbox01.setObjectName("checkbox01")
        self.label03_2 = QtWidgets.QLabel(self.centralwidget)
        self.label03_2.setGeometry(QtCore.QRect(210, 480, 161, 21))
        self.label03_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label03_2.setLineWidth(8)
        self.label03_2.setObjectName("label03_2")
        simple_pizza_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(simple_pizza_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        simple_pizza_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(simple_pizza_window)
        self.statusbar.setObjectName("statusbar")
        simple_pizza_window.setStatusBar(self.statusbar)

        self.retranslateUi(simple_pizza_window)
        QtCore.QMetaObject.connectSlotsByName(simple_pizza_window)

    def retranslateUi(self, simple_pizza_window):
        _translate = QtCore.QCoreApplication.translate
        simple_pizza_window.setWindowTitle(_translate("simple_pizza_window", "Simple 3 Ingredient Pizza"))
        self.button06.setText(_translate("simple_pizza_window", "Proceed To Payment"))
        self.r_button03.setText(_translate("simple_pizza_window", "Normal"))
        self.r_button01.setText(_translate("simple_pizza_window", "Spicy "))
        self.r_button02.setText(_translate("simple_pizza_window", "Mild"))
        self.label03.setText(_translate("simple_pizza_window", "Choose Your Sauce"))
        self.checkbox02.setText(_translate("simple_pizza_window", "Unsliced"))
        self.checkbox01.setText(_translate("simple_pizza_window", "Sliced"))
        self.label03_2.setText(_translate("simple_pizza_window", "How Do You Want Your Pizza"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    simple_pizza_window = QtWidgets.QMainWindow()
    ui = Ui_simple_pizza_window()
    ui.setupUi(simple_pizza_window)

    simple_pizza_window.show()
    sys.exit(app.exec_())
