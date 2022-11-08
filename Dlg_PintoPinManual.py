from time import sleep

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, qApp, QHeaderView

from Ui_Pin_to_Pin_Manual import Ui_Dialog_Pin_to_Pin_Manual
from Reports_Generator import Get_Reports


class Pin_to_Pin_ManualDlg(QDialog,Ui_Dialog_Pin_to_Pin_Manual):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.min=0
        self.max=5
        self.AbortTestFlag = False
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)

        self.pushButton_Measure.clicked.connect(self.fun_measure)
        self.pushButton_Abort.clicked.connect(self.AbortTest)
        self.pushButton_Save.clicked.connect(self.SaveReport)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setDisabled(True)

        self.comboBox_LineX.clear()
        self.comboBox_From.clear()
        self.comboBox_To.clear()

        for i in range(0,128):
            self.comboBox_LineX.addItem("PIN-"+str(i+1))
            self.comboBox_From.addItem("PIN-"+str(i+1))
            self.comboBox_To.addItem("PIN-"+str(i+1))

        self.comboBox_From.currentIndexChanged.connect(self.changeindex)

        self.progressBar.setValue(0)

    def closewindow(self):
        self.close()

    def AbortTest(self):
        msg = QMessageBox.critical(self,"","Do you want to continue",QMessageBox.Yes|QMessageBox.No)
        if msg==QMessageBox.Yes:
            self.AbortTestFlag = True
            self.tableWidget.setRowCount(self.tableWidget.currentRow()+1)
            self.pushButton_Back.setEnabled(True)
            self.pushButton_Save.setEnabled(True)
        else:
            self.AbortTestFlag = False
            self.pushButton_Back.setDisabled(True)
            self.pushButton_Save.setDisabled(True)

    def fun_measure(self):
        inputfrom = int(self.comboBox_From.currentIndex())
        inputto = int(self.comboBox_To.currentText()[4:])
        range = inputto-inputfrom+1
        print(inputto,inputfrom,range)
        self.pushButton_Abort.setEnabled(True)
        self.pushButton_Back.setDisabled(True)
        self.pushButton_Save.setDisabled(True)
        self.tableWidget.setRowCount(0)
        self.AbortTestFlag = False
        measured_value = 4.5
        self.tableWidget.setRowCount(range-1)
        i = 0
        while (self.AbortTestFlag == False) and (i < range):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.comboBox_LineX.currentText())))
            self.tableWidget.setItem(i, 2, QTableWidgetItem("PIN-" + str(inputfrom+1)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.min)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(measured_value)))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.max)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))
            if measured_value > self.min and measured_value < self.max:
                self.tableWidget.setItem(i, 7, QTableWidgetItem("PASS"))
            else:
                self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
            self.tableWidget.selectRow(i)
            self.progressBar.setValue(int((i + 1) * 100 / range))
            qApp.processEvents()
            sleep(0.1)
            i = i + 1
            inputfrom+=1
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setEnabled(True)
        print("measure")

    def SaveReport(self):
        Get_Reports().Generate_Report_PTPMan(self.tableWidget)

    def changeindex(self):
        index = self.comboBox_From.currentIndex()
        self.comboBox_To.clear()
        for i in range(index,128):
            self.comboBox_To.addItem("PIN-"+str(i+1))