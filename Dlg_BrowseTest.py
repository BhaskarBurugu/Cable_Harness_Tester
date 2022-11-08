from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from openpyxl import load_workbook

from Ui_Browse_Test import Ui_Dialog_BrowseTest

import pandas as pd
class BrowseTestDlg(QDialog,Ui_Dialog_BrowseTest):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)

        self.pushButton_Measure.clicked.connect(self.fun_measure)

        self.pushButton_Browse.clicked.connect(self.fun_browse)

        self.progressBar.setValue(0)

    def closewindow(self):
        self.close()

    def fun_measure(self):
        print("measure")

    def fun_browse(self):
        frompinlist = []
        topinlist = []
        minvallist = []
        maxvallist = []
        workbook = load_workbook(filename="Input File.xlsx")
        sheet = workbook.active
        nr = sheet.max_row
        for i in range(8, nr):
            frompinlist.append(sheet.cell(i, 1).value)
            topinlist.append(sheet.cell(i,3).value)
            minvallist.append(sheet.cell(i,6).value)
            maxvallist.append(sheet.cell(i, 7).value)
        self.tableWidget.setRowCount(nr-8)
        for i in range(0,nr-8):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem("PIN-" + str(frompinlist[i])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem("PIN-" + str(topinlist[i])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(minvallist[i])))

            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(maxvallist[i])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))
