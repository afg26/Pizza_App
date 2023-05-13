

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_payment_window(object):
    def setupUi(self, payment_window):
        payment_window.setObjectName("payment_window")
        payment_window.resize(422, 395)
        self.centralwidget = QtWidgets.QWidget(payment_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setLineWidth(8)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.paid_cash())
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked =lambda : self.count())
        self.pushButton_2.setGeometry(QtCore.QRect(224, 60, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 270, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.button09 = QtWidgets.QPushButton(self.centralwidget, clicked =lambda : self.print_receipt())
        self.button09.setGeometry(QtCore.QRect(40, 310, 341, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button09.setFont(font)
        self.button09.setObjectName("button09")

        self.button10 = QtWidgets.QPushButton(self.centralwidget, clicked =lambda : self.simple_pizza())
        self.button10.setGeometry(QtCore.QRect(40, 340, 341, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(70)
        self.button10.setFont(font)
        self.button10.setObjectName("button10")

        self.tb_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.tb_2.setGeometry(QtCore.QRect(220, 150, 161, 20))
        self.tb_2.setObjectName("tb_2")
        self.tb_2.setEnabled(False)


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 120, 161, 21))
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setLineWidth(2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 180, 161, 21))
        self.label_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setLineWidth(2)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 210, 161, 21))
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setLineWidth(2)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 240, 161, 21))
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setLineWidth(2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 270, 161, 21))
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setLineWidth(2)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        payment_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(payment_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        payment_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(payment_window)
        self.statusbar.setObjectName("statusbar")
        payment_window.setStatusBar(self.statusbar)

        self.retranslateUi(payment_window)
        QtCore.QMetaObject.connectSlotsByName(payment_window)

    def retranslateUi(self, payment_window):
        _translate = QtCore.QCoreApplication.translate
        payment_window.setWindowTitle(_translate("payment_window", "MainWindow"))
        self.label.setText(_translate("payment_window", "Payment."))
        self.label_2.setText(_translate("payment_window", "Bill"))
        self.pushButton.setText(_translate("payment_window", "Cash"))
        self.pushButton_2.setText(_translate("payment_window", "Card"))
        self.label_4.setText(_translate("payment_window", "Paid Cash"))
        self.label_3.setText(_translate("payment_window", "Tip"))
        self.label_5.setText(_translate("payment_window", "7% S-Tax]"))
        self.label_6.setText(_translate("payment_window", "Total Bill"))
        self.label_7.setText(_translate("payment_window", "Change "))
        self.button09.setText(_translate("payment_window", "Print Receipt"))
        self.button10.setText(_translate("payment_window", "Print Receipt For Simple Pizza "))

    def count(self):

        self.bill = round((self.protein + self.vegetable) , 2)
        self.label_8.setText(str("%.2f" % self.bill))

        self.tip = round((self.bill * 0.01) ,2)
        self.label_9.setText(str("%.2f" % self.tip))

        self.tax  =round((self.bill * 0.07), 2)
        self.label_10.setText(str("%.2f" % self.tax))

        self.total_bill= round((self.bill + self.tax + self.tip) , 2)
        self.label_11.setText(str("%.2f" % self.total_bill))
        self.tb_2.setEnabled(True)

    def simple_pizza(self):

        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.tb_2.setEnabled(False)

        f = open("receipt.txt", "w")

        if self.sauce2 == "Spicy":

            f.write("You Have Chosen a Spicy Sauce" + "\n")

            self.bill1 = 9.50

            self.label_8.setText(str("%.2f" % self.bill1))

            self.tip1 = round((self.bill1 * 0.10) , 2)
            self.label_9.setText(str("%.2f" % self.tip1))

            self.tax1 = round((self.bill1 * 0.07), 2)
            self.label_10.setText(str("%.2f" % self.tax1))

            self.total_bill1 = round((self.bill1 + self.tax1 + self.tip1) , 2)
            self.label_11.setText(str("%.2f" % self.total_bill1))
            self.tb_2.setEnabled(True)

        elif self.sauce2 == "Mild" :
            f.write("You Have Chosen a Mild Sauce" + "\n")

            self.bill1 = 9.50

            self.label_8.setText(str("%.2f" % self.bill1))

            self.tip1 = round((self.bill1 * 0.10) , 2)
            self.label_9.setText(str("%.2f" % self.tip1))

            self.tax1 = round((self.bill1 * 0.07), 2)
            self.label_10.setText(str("%.2f" % self.tax1))

            self.total_bill1 = round((self.bill1 + self.tax1 + self.tip1) , 2)
            self.label_11.setText(str("%.2f" % self.total_bill1))
            self.tb_2.setEnabled(True)


        elif self.sauce2 == "Normal" :
            f.write("You Have Chosen a Normal Sauce" + "\n")

            self.bill1 = 9.50

            self.label_8.setText(str("%.2f" % self.bill1))

            self.tip1 = round((self.bill1 * 0.10) , 2)
            self.label_9.setText(str("%.2f" % self.tip1))

            self.tax1 = round((self.bill1 * 0.07), 2)
            self.label_10.setText(str("%.2f" % self.tax1))

            self.total_bill1 = round((self.bill1 + self.tax1 + self.tip1) , 2)
            self.label_11.setText(str("%.2f" % self.total_bill1))
            self.tb_2.setEnabled(True)


        if self.type2 == "Sliced":
            f.write("You Have Chosen Your Pizza to be Sliced" + "\n")
        if self.type2 == "UnSliced":
            f.write("You Have Chosen Your Pizza to be UnSliced" + "\n")



        tip1 = self.label_9.text()
        tax1 = str(self.tax1)
        bill1 = str(self.bill1)
        total1 = str(self.total_bill1)
        

        f.write("Bill            :    " + bill1 + "\n")
        f.write("Tip             :    " + tip1 + "\n")
        f.write("7 % tax         :    " + tax1 + "\n")
        f.write("Total_Bill      :    " + total1 + "\n")
        f.close()

        # open and read the file after the overwriting:
        f = open("receipt.txt", "r")
        print(f.read())



    def paid_cash(self):
        self.change = float(self.tb_2.text()) - float(self.total_bill)
        self.label_12.setText(str("%.2f" % self.change))

    def print_receipt(self):

        f = open("receipt.txt", "w")

        if self.protein == 8.50 :
            f.write("You Have Chosen a Chicken Pizza"  + "\n")
        elif self.protein == 10.50:
            f.write("You Have Chosen a Beef Pizza" + "\n")
        elif self.protein == 11.50:
            f.write("You Have Chosen a Fish Pizza" + "\n")

        if self.sauce == "Spicy" :
            f.write("You Have Chosen a Spicy Sauce" + "\n")
        if self.sauce == "Mild" :
            f.write("You Have Chosen a Mild Sauce" + "\n")
        if self.sauce == "Normal" :
            f.write("You Have Chosen a Normal Sauce" + "\n")

        if self.type == "Sliced":
            f.write("You Have Chosen Your Pizza to be Sliced" + "\n")
        if self.type == "UnSliced":
            f.write("You Have Chosen Your Pizza to be UnSliced" + "\n")


        tip = self.label_9.text()
        tax = str(self.tax)
        bill = str(self.bill)
        total = str(self.total_bill)

        f.write("Bill            :    " + bill + "\n")
        f.write("Tip             :    " + tip + "\n")
        f.write("7 % tax         :    " + tax + "\n")
        f.write("Total_Bill      :    " +  total + "\n")
        f.close()

        # open and read the file after the overwriting:
        f = open("receipt.txt", "r")
        print(f.read())

    def receive_data(self, vegetable, protein, sauce, type):

        self.vegetable = vegetable
        self.protein = protein
        self.sauce = sauce
        self.type = type

    def receive_data2(self, sauce2, type2):
        self.sauce2 = sauce2
        self.type2 = type2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    payment_window = QtWidgets.QMainWindow()
    ui = Ui_payment_window()
    ui.setupUi(payment_window)
    payment_window.show()
    sys.exit(app.exec_())
