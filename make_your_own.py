from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from payment import Ui_payment_window


class Ui_make_your_own_window(object):

    def open_payment(self):
        self.payment = QtWidgets.QMainWindow()
        self.payment_ui = Ui_payment_window()
        self.payment_ui.setupUi(self.payment)
        self.payment.show()

    def setupUi(self, make_your_own_window):
        make_your_own_window.setObjectName("make_your_own_window")
        make_your_own_window.resize(905, 630)
        self.centralwidget = QtWidgets.QWidget(make_your_own_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 871, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image02.JPG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 490, 161, 16))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 490, 281, 16))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 490, 231, 16))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setObjectName("label_5")
        self.button07 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.fetch_data)
        self.button07.setGeometry(QtCore.QRect(660, 560, 231, 23))
        self.button07.setObjectName("button07")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 510, 161, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.r_button04 = QtWidgets.QRadioButton(self.frame)
        self.r_button04.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.r_button04.setObjectName("r_button04")
        self.r_button05 = QtWidgets.QRadioButton(self.frame)
        self.r_button05.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.r_button05.setObjectName("r_button05")
        self.r_button06 = QtWidgets.QRadioButton(self.frame)
        self.r_button06.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.r_button06.setObjectName("r_button06")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 490, 161, 16))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(190, 510, 161, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.checkbox03 = QtWidgets.QCheckBox(self.frame_2)


        self.checkbox03.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.checkbox03.setObjectName("checkbox03")

        self.checkbox04 = QtWidgets.QCheckBox(self.frame_2)
        self.checkbox04.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.checkbox04.setObjectName("checkbox04")
        self.checkbox05 = QtWidgets.QCheckBox(self.frame_2)
        self.checkbox05.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkbox05.setObjectName("checkbox05")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(110, 10, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(110, 50, 47, 13))
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(360, 510, 281, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.checkbox06 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox06.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.checkbox06.setObjectName("checkbox06")
        self.checkbox07 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox07.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.checkbox07.setObjectName("checkbox07")
        self.checkbox08 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox08.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkbox08.setObjectName("checkbox08")
        self.checkbox09 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox09.setGeometry(QtCore.QRect(100, 10, 81, 17))
        self.checkbox09.setObjectName("checkbox09")
        self.checkbox10 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox10.setGeometry(QtCore.QRect(100, 30, 70, 17))
        self.checkbox10.setObjectName("checkbox10")
        self.checkbox12 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox12.setGeometry(QtCore.QRect(100, 50, 81, 17))
        self.checkbox12.setObjectName("checkbox12")
        self.checkbox11 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox11.setGeometry(QtCore.QRect(200, 10, 70, 17))
        self.checkbox11.setObjectName("checkbox11")
        self.checkbox13 = QtWidgets.QCheckBox(self.frame_3)
        self.checkbox13.setGeometry(QtCore.QRect(200, 30, 81, 17))
        self.checkbox13.setObjectName("checkbox13")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(660, 510, 231, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(3)
        self.frame_4.setObjectName("frame_4")
        self.checkbox14 = QtWidgets.QCheckBox(self.frame_4)
        self.checkbox14.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.checkbox14.setObjectName("checkbox14")
        self.checkbox15 = QtWidgets.QCheckBox(self.frame_4)
        self.checkbox15.setGeometry(QtCore.QRect(150, 10, 70, 17))
        self.checkbox15.setObjectName("checkbox15")
        make_your_own_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(make_your_own_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        make_your_own_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(make_your_own_window)
        self.statusbar.setObjectName("statusbar")
        make_your_own_window.setStatusBar(self.statusbar)

        self.retranslateUi(make_your_own_window)
        QtCore.QMetaObject.connectSlotsByName(make_your_own_window)





    def retranslateUi(self, make_your_own_window):
        _translate = QtCore.QCoreApplication.translate
        make_your_own_window.setWindowTitle(_translate("make_your_own_window", "Make Your Own"))
        self.label_3.setText(_translate("make_your_own_window", "Choose your Protien"))
        self.label_4.setText(_translate("make_your_own_window", "Choose Your Vegetables         $ 0.75  ea"))
        self.label_5.setText(_translate("make_your_own_window", "How Do You Want Your Pizza"))
        self.button07.setText(_translate("make_your_own_window", "Proceed To Payment"))
        self.r_button04.setText(_translate("make_your_own_window", "Spicy"))
        self.r_button05.setText(_translate("make_your_own_window", "Mild"))
        self.r_button06.setText(_translate("make_your_own_window", "Normal"))
        self.label_2.setText(_translate("make_your_own_window", "Choose your Sauce"))
        self.checkbox03.setText(_translate("make_your_own_window", "Beef"))
        self.checkbox04.setText(_translate("make_your_own_window", "Chicken"))
        self.checkbox05.setText(_translate("make_your_own_window", "Fish"))
        self.label_6.setText(_translate("make_your_own_window", "$ 10.50"))
        self.label_7.setText(_translate("make_your_own_window", "$ 08.50"))
        self.label_8.setText(_translate("make_your_own_window", "$ 11.50"))
        self.checkbox06.setText(_translate("make_your_own_window", "Mashrooms"))
        self.checkbox07.setText(_translate("make_your_own_window", "Onions"))
        self.checkbox08.setText(_translate("make_your_own_window", "Tomatoes"))
        self.checkbox09.setText(_translate("make_your_own_window", "Pickles"))
        self.checkbox10.setText(_translate("make_your_own_window", "Bell Peper"))
        self.checkbox12.setText(_translate("make_your_own_window", "Black Olives"))
        self.checkbox11.setText(_translate("make_your_own_window", "Chili"))
        self.checkbox13.setText(_translate("make_your_own_window", "Pineapples"))
        self.checkbox14.setText(_translate("make_your_own_window", "Sliced"))
        self.checkbox15.setText(_translate("make_your_own_window", "Chicken"))

class Get_data(Ui_make_your_own_window):

    def fetch_data(self):











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    make_your_own_window = QtWidgets.QMainWindow()
    ui = Ui_make_your_own_window()
    ui.setupUi(make_your_own_window)





    make_your_own_window.show()
    sys.exit(app.exec_())
