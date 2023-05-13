# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\about_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(461, 466)
        about_window.setFocusPolicy(QtCore.Qt.StrongFocus)
        about_window.setAcceptDrops(False)
        about_window.setAutoFillBackground(False)
        about_window.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(about_window)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 230, 441, 191))

        self.plainTextEdit.setEnabled(False)

        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 200, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 10, 441, 191))
        self.plainTextEdit_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setAutoFillBackground(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        about_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(about_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")
        about_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(about_window)
        self.statusbar.setObjectName("statusbar")
        about_window.setStatusBar(self.statusbar)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("about_window", "While topped flatbreads were consumed in ancient "
                                                                   "Egypt, and Rome, Italians are credited as the"
                                                                   " people who invented pizza first. During the 1700s"
                                                                   " and 1800s, Naples was a bustling waterfront "
                                                                   "city especially near the shore, where overcrowding"
                                                                   " and primarily outdoor living forced locals to find"
                                                                   " quick, easy ways to feed their families, and it"
                                                                   "became a common dish because of its limited "
                                                                   "ingredients and handy portability, but it was "
                                                                   "considered a street food for the poor, unsuitable "
                                                                   "for the upper class."))
        self.label.setText(_translate("about_window", "A Breif History of Pizza"))
        self.plainTextEdit_2.setPlainText(_translate("about_window", "Pizza Ordering Application ( Text Edition)\n"
"\n"
"Build # PC- 05.12.2023, built on May 12,  2023\n"

"Runtime Version:17.0.6+1-b653.34 amd64\n"
"VM: Opensource and Milestone for SDEV 140\n"
"\n"
"Powered by simple programming just for learning\n"
"Copyright © free for everyone to learn\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QMainWindow()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec_())

