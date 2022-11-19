import datetime
import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QBrush
from PyQt5.QtWidgets import *

from openpyxl import load_workbook
from openpyxl.styles import Side, Border
from Ui_SelfTest import Ui_Dialog_SelfTest


#################################################################################################################
class FaultReportDlg(QDialog,Ui_Dialog_SelfTest):
    def __init__(self,parent = None,):
        super().__init__(parent)
        self.setupUi(self)

        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)
        self.tableWidget.setRowCount(128)
        self.label.resize(500,30)
        self.label.move(300,20)
        self.GUI=None
        self.pushButton_Save.clicked.connect(self.SaveReport)
        self.pushButton_Save.hide()
        self.pushButton_Abort.hide()
        self.progressBar.hide()
        self.pushButton_Measure.hide()
        self.faultypoints = 0
    ################################################################################################################
    def closewindow(self):
        self.close()
    def SaveReport(self):
        template = f'''Reports/{self.GUI}/{self.GUI}Template.xlsx'''
        outfile = f'''Reports/{self.GUI}/{self.GUI}_FaultReport'''+datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')+'.xlsx'
        workbook = load_workbook(filename=template)
        # open workbook
        sheet = workbook.active

        for i in range(0,self.tableWidget.rowCount()):
            sheet[f'''A{i+8}'''] = self.tableWidget.item(i,0).text()
            sheet[f'''B{i + 8}'''] = self.tableWidget.item(i, 1).text()
            sheet[f'''C{i + 8}'''] = self.tableWidget.item(i, 2).text()
            sheet[f'''D{i + 8}'''] = self.tableWidget.item(i, 3).text()
            sheet[f'''E{i + 8}'''] = self.tableWidget.item(i, 4).text()
            sheet[f'''F{i + 8}'''] = self.tableWidget.item(i, 5).text()
            sheet[f'''G{i + 8}'''] = self.tableWidget.item(i, 6).text()
            sheet[f'''H{i + 8}'''] = self.tableWidget.item(i, 7).text()

        self.set_border(sheet, f'''A8:H{8+i}''')

        # save the file
        workbook.save(filename=outfile)
        QMessageBox.information(self,self.GUI,"Reports Saved to "+outfile)
    #################################################################################################################
    def set_border(self,worksheet, cell_range):
        thin = Side(border_style="thin", color="000000")
        for row in worksheet[cell_range]:
            for cell in row:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)