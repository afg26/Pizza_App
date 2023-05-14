
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_window(object):
    def setupUi(self, help_window):
        help_window.setObjectName("help_window")
        help_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(help_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 761, 501))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        help_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(help_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        help_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(help_window)
        self.statusbar.setObjectName("statusbar")
        help_window.setStatusBar(self.statusbar)

        self.retranslateUi(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate("help_window", "MainWindow"))
        self.label.setText(_translate("help_window", "How To Use The App."))
        self.plainTextEdit.setPlainText(_translate("help_window", "*-     The usage of this app is very easy, the main interface is the main page which has 5 button         and performing different task.\n"
"\n"
"*-    The \"Create Your Own\" button takes you to a new window which you have option of\n"
"    choosing different ingredients of making your own pizza and by clicking on \"Proceed to \n"
"    Payment\" button the payment page gets open and you click on \"Card\" to calculate your \n"
"    bill and there is \"Textbox\" that gets enabled if you want to pay cash you add your amount\n"
"    on that textbox and click on \"Cash\" button to calculate the cash entry and then you click \n"
"    on \"Print Receipt\" button to write your file on a text file and it also gives you the output in\n"
"    the terminal too.\n"
"\n"
"*-    The next buttton is \"Simple 3 Ingredeint Pizza\" which takes you to a new page with only \n"
"    having to  choose between two option with different types and then you click on the\n"
"    \"Proceed to Payment\" page for payment, here for calculating your bill you have click\n"
"    only on \"Print Receipt for Simple Pizza\" and it will calculate it  and write it to a text file\n"
"    and print it on the terminal.\n"
"*-    The next button is \"About\" which I have added a small breif history of pizza and a\n"
"    simple version information.\n"
"\n"
"*-    The next button is \"Help\" which opens this window.\n"
"\n"
"*-    The last button is \"Exit\" which closes the main window.\n"
"\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_window = QtWidgets.QMainWindow()
    ui = Ui_help_window()
    ui.setupUi(help_window)
    help_window.show()
    sys.exit(app.exec_())

