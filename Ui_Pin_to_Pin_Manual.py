# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pin_to_Pin_Manual.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Pin_to_PinManual(object):
    def setupUi(self, Dialog_Pin_to_PinManual):
        Dialog_Pin_to_PinManual.setObjectName("Dialog_Pin_to_PinManual")
        Dialog_Pin_to_PinManual.resize(1024, 720)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Pin_to_PinManual)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 891, 461))
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
        self.progressBar = QtWidgets.QProgressBar(Dialog_Pin_to_PinManual)
        self.progressBar.setGeometry(QtCore.QRect(60, 620, 931, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.comboBox_LineX = QtWidgets.QComboBox(Dialog_Pin_to_PinManual)
        self.comboBox_LineX.setGeometry(QtCore.QRect(280, 110, 111, 22))
        self.comboBox_LineX.setObjectName("comboBox_LineX")
        self.comboBox_LineX.addItem("")
        self.label_Units_2 = QtWidgets.QLabel(Dialog_Pin_to_PinManual)
        self.label_Units_2.setGeometry(QtCore.QRect(280, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Units_2.setFont(font)
        self.label_Units_2.setObjectName("label_Units_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog_Pin_to_PinManual)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 640, 691, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Measure = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Measure.setFont(font)
        self.pushButton_Measure.setObjectName("pushButton_Measure")
        self.horizontalLayout.addWidget(self.pushButton_Measure)
        self.pushButton_Save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout.addWidget(self.pushButton_Save)
        self.pushButton_Abort = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Abort.setFont(font)
        self.pushButton_Abort.setObjectName("pushButton_Abort")
        self.horizontalLayout.addWidget(self.pushButton_Abort)
        self.pushButton_Back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout.addWidget(self.pushButton_Back)
        self.label = QtWidgets.QLabel(Dialog_Pin_to_PinManual)
        self.label.setGeometry(QtCore.QRect(310, 0, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 0, 127);")
        self.label.setObjectName("label")
        self.LineY = QtWidgets.QFrame(Dialog_Pin_to_PinManual)
        self.LineY.setGeometry(QtCore.QRect(410, 70, 331, 71))
        self.LineY.setBaseSize(QtCore.QSize(0, 0))
        self.LineY.setFrameShape(QtWidgets.QFrame.Box)
        self.LineY.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineY.setObjectName("LineY")
        self.label_Units_5 = QtWidgets.QLabel(self.LineY)
        self.label_Units_5.setGeometry(QtCore.QRect(120, 0, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Units_5.setFont(font)
        self.label_Units_5.setObjectName("label_Units_5")
        self.label_Units_4 = QtWidgets.QLabel(self.LineY)
        self.label_Units_4.setGeometry(QtCore.QRect(250, 10, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Units_4.setFont(font)
        self.label_Units_4.setObjectName("label_Units_4")
        self.label_Units_3 = QtWidgets.QLabel(self.LineY)
        self.label_Units_3.setGeometry(QtCore.QRect(20, 10, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Units_3.setFont(font)
        self.label_Units_3.setObjectName("label_Units_3")
        self.comboBox_From = QtWidgets.QComboBox(self.LineY)
        self.comboBox_From.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.comboBox_From.setObjectName("comboBox_From")
        self.comboBox_From.addItem("")
        self.comboBox_To = QtWidgets.QComboBox(self.LineY)
        self.comboBox_To.setGeometry(QtCore.QRect(210, 40, 111, 22))
        self.comboBox_To.setObjectName("comboBox_To")
        self.comboBox_To.addItem("")
        self.label_Units_2.setBuddy(self.comboBox_LineX)
        self.label_Units_5.setBuddy(self.comboBox_LineX)
        self.label_Units_4.setBuddy(self.comboBox_To)
        self.label_Units_3.setBuddy(self.comboBox_From)

        self.retranslateUi(Dialog_Pin_to_PinManual)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Pin_to_PinManual)
        Dialog_Pin_to_PinManual.setTabOrder(self.tableWidget, self.comboBox_LineX)
        Dialog_Pin_to_PinManual.setTabOrder(self.comboBox_LineX, self.comboBox_From)
        Dialog_Pin_to_PinManual.setTabOrder(self.comboBox_From, self.comboBox_To)
        Dialog_Pin_to_PinManual.setTabOrder(self.comboBox_To, self.pushButton_Measure)
        Dialog_Pin_to_PinManual.setTabOrder(self.pushButton_Measure, self.pushButton_Save)
        Dialog_Pin_to_PinManual.setTabOrder(self.pushButton_Save, self.pushButton_Abort)
        Dialog_Pin_to_PinManual.setTabOrder(self.pushButton_Abort, self.pushButton_Back)

    def retranslateUi(self, Dialog_Pin_to_PinManual):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Pin_to_PinManual.setWindowTitle(_translate("Dialog_Pin_to_PinManual", "Pin to Pin Manual"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Pin_to_PinManual", "S.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Line X"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Pin_to_PinManual", "LineY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Min"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Measured Value"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Max"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Units"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_Pin_to_PinManual", "Results"))
        self.comboBox_LineX.setItemText(0, _translate("Dialog_Pin_to_PinManual", "PIN-1"))
        self.label_Units_2.setText(_translate("Dialog_Pin_to_PinManual", "Line X"))
        self.pushButton_Measure.setText(_translate("Dialog_Pin_to_PinManual", "&Measure"))
        self.pushButton_Save.setText(_translate("Dialog_Pin_to_PinManual", "&Save"))
        self.pushButton_Abort.setText(_translate("Dialog_Pin_to_PinManual", "&Abort"))
        self.pushButton_Back.setText(_translate("Dialog_Pin_to_PinManual", "&Close"))
        self.label.setText(_translate("Dialog_Pin_to_PinManual", "Pin to Pin Manual Test"))
        self.label_Units_5.setText(_translate("Dialog_Pin_to_PinManual", "Line Y"))
        self.label_Units_4.setText(_translate("Dialog_Pin_to_PinManual", "To:"))
        self.label_Units_3.setText(_translate("Dialog_Pin_to_PinManual", "From:"))
        self.comboBox_From.setItemText(0, _translate("Dialog_Pin_to_PinManual", "PIN-2"))
        self.comboBox_To.setItemText(0, _translate("Dialog_Pin_to_PinManual", "PIN-128"))
