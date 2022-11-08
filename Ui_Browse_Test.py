# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Browse_Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_BrowseTest(object):
    def setupUi(self, Dialog_BrowseTest):
        Dialog_BrowseTest.setObjectName("Dialog_BrowseTest")
        Dialog_BrowseTest.resize(1030, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logos/logotrspisq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_BrowseTest.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_BrowseTest)
        self.tableWidget.setGeometry(QtCore.QRect(10, 71, 1011, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_Measure = QtWidgets.QPushButton(Dialog_BrowseTest)
        self.pushButton_Measure.setGeometry(QtCore.QRect(10, 590, 93, 28))
        self.pushButton_Measure.setObjectName("pushButton_Measure")
        self.pushButton_Save = QtWidgets.QPushButton(Dialog_BrowseTest)
        self.pushButton_Save.setGeometry(QtCore.QRect(130, 590, 93, 28))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Abort = QtWidgets.QPushButton(Dialog_BrowseTest)
        self.pushButton_Abort.setGeometry(QtCore.QRect(240, 590, 93, 28))
        self.pushButton_Abort.setObjectName("pushButton_Abort")
        self.pushButton_Back = QtWidgets.QPushButton(Dialog_BrowseTest)
        self.pushButton_Back.setGeometry(QtCore.QRect(350, 590, 93, 28))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.progressBar = QtWidgets.QProgressBar(Dialog_BrowseTest)
        self.progressBar.setGeometry(QtCore.QRect(470, 590, 551, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_SFP = QtWidgets.QLabel(Dialog_BrowseTest)
        self.label_SFP.setGeometry(QtCore.QRect(50, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SFP.setFont(font)
        self.label_SFP.setObjectName("label_SFP")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_BrowseTest)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 671, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_Browse = QtWidgets.QPushButton(Dialog_BrowseTest)
        self.pushButton_Browse.setGeometry(QtCore.QRect(820, 20, 51, 31))
        self.pushButton_Browse.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/BT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Browse.setIcon(icon)
        self.pushButton_Browse.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Browse.setFlat(False)
        self.pushButton_Browse.setObjectName("pushButton_Browse")

        self.retranslateUi(Dialog_BrowseTest)
        QtCore.QMetaObject.connectSlotsByName(Dialog_BrowseTest)

    def retranslateUi(self, Dialog_BrowseTest):
        _translate = QtCore.QCoreApplication.translate
        Dialog_BrowseTest.setWindowTitle(_translate("Dialog_BrowseTest", "Browse Test"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_BrowseTest", "S.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_BrowseTest", "Line X"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_BrowseTest", "LineY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_BrowseTest", "Min"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_BrowseTest", "Measured Value"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_BrowseTest", "Max"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_BrowseTest", "Units"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_BrowseTest", "Results"))
        self.pushButton_Measure.setText(_translate("Dialog_BrowseTest", "Measure"))
        self.pushButton_Save.setText(_translate("Dialog_BrowseTest", "Save"))
        self.pushButton_Abort.setText(_translate("Dialog_BrowseTest", "Abort"))
        self.pushButton_Back.setText(_translate("Dialog_BrowseTest", "Back"))
        self.label_SFP.setText(_translate("Dialog_BrowseTest", "Select File:"))