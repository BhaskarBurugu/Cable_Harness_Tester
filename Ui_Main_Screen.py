# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logos/logotrspisq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelf_Test = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/SlfTst.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelf_Test.setIcon(icon)
        self.actionSelf_Test.setObjectName("actionSelf_Test")
        self.actionDiode_Test = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/DidTst.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDiode_Test.setIcon(icon1)
        self.actionDiode_Test.setObjectName("actionDiode_Test")
        self.actionPin_to_Pin_Automatic = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/PtPAut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPin_to_Pin_Automatic.setIcon(icon2)
        self.actionPin_to_Pin_Automatic.setObjectName("actionPin_to_Pin_Automatic")
        self.actionPin_to_Pin_Manual = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/PtPMan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPin_to_Pin_Manual.setIcon(icon3)
        self.actionPin_to_Pin_Manual.setObjectName("actionPin_to_Pin_Manual")
        self.actionBrowse_Test = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/Browse import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrowse_Test.setIcon(icon4)
        self.actionBrowse_Test.setObjectName("actionBrowse_Test")
        self.actionManual_Test = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/MT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManual_Test.setIcon(icon5)
        self.actionManual_Test.setObjectName("actionManual_Test")
        self.toolBar.addAction(self.actionSelf_Test)
        self.toolBar.addAction(self.actionDiode_Test)
        self.toolBar.addAction(self.actionPin_to_Pin_Automatic)
        self.toolBar.addAction(self.actionPin_to_Pin_Manual)
        self.toolBar.addAction(self.actionBrowse_Test)
        self.toolBar.addAction(self.actionManual_Test)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSelf_Test.setText(_translate("MainWindow", "Self Test"))
        self.actionDiode_Test.setText(_translate("MainWindow", "Diode Test"))
        self.actionPin_to_Pin_Automatic.setText(_translate("MainWindow", "Pin to Pin Automatic"))
        self.actionPin_to_Pin_Manual.setText(_translate("MainWindow", "Pin to Pin Manual"))
        self.actionBrowse_Test.setText(_translate("MainWindow", "Browse Test"))
        self.actionManual_Test.setText(_translate("MainWindow", "Manual Test"))
