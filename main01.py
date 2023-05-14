from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from  make_your_own import Ui_make_your_own_window
from simple_pizza import Ui_simple_pizza_window
from about_window import Ui_about_window
from help_window import Ui_help_window




class Ui_MainWindow(object):
    def open_simple_pizza(self ):
        self.simple_pizza= main_simple_pizza
        self.simple_pizza.show()

    def open_make_your_own(self):
        self.make_your = main_make_your_own
        self.make_your.show()

    def about_window(self):
        self.__about = about
        self.__about.show()

    def help_window(self):
        self._help = open_help
        self._help.show()



    def close_window(self):
        self.MainWindow.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 871, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image_01.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 480, 871, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.button05 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.close_window())
        self.button05.setGeometry(QtCore.QRect(700, 10, 141, 28))
        self.button05.setObjectName("button05")
        self.button01 = QtWidgets.QPushButton(self.frame,  clicked = lambda: self.open_make_your_own())
        self.button01.setGeometry(QtCore.QRect(20, 10, 141, 28))
        self.button01.setObjectName("button01")
        self.button02 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.open_simple_pizza())
        self.button02.setGeometry(QtCore.QRect(190, 10, 141, 28))
        self.button02.setObjectName("button02")
        self.button03 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.about_window())
        self.button03.setGeometry(QtCore.QRect(360, 10, 141, 28))
        self.button03.setObjectName("button03")
        self.button04 = QtWidgets.QPushButton(self.frame, clicked = lambda: self._help())
        self.button04.setGeometry(QtCore.QRect(530, 10, 141, 28))
        self.button04.setObjectName("button04")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button05.setText(_translate("MainWindow", "Exit"))
        self.button01.setText(_translate("MainWindow", "Create Your Own"))
        self.button02.setText(_translate("MainWindow", "Simple 3 Ingredeints Pizza"))
        self.button03.setText(_translate("MainWindow", "About"))
        self.button04.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    main_make_your_own = QtWidgets.QMainWindow()
    make_your_own_ui = Ui_make_your_own_window()
    make_your_own_ui.setupUi(main_make_your_own)

    main_simple_pizza = QtWidgets.QMainWindow()
    simple_pizza_ui = Ui_simple_pizza_window()
    simple_pizza_ui.setupUi(main_simple_pizza)

    about = QtWidgets.QMainWindow()
    about_window_ui = Ui_about_window()
    about_window_ui.setupUi(about)

    open_help = QtWidgets.QMainWindow()
    help_window_ui = Ui_help_window()
    help_window_ui.setupUi(open_help)

    MainWindow.show()
    sys.exit(app.exec_())
