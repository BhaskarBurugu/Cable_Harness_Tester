from PyQt5.QtWidgets import QDialog, QHeaderView
from Ui_DiodeTest import Ui_Dialog_DiodeTest

class DiodeTestDlg(QDialog,Ui_Dialog_DiodeTest):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)

        self.pushButton_Measure.clicked.connect(self.fun_measure)

        self.progressBar.setValue(0)

    def closewindow(self):
        self.close()

    def fun_measure(self):
        print("measure")