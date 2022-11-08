from PyQt5.QtWidgets import QDialog

from Ui_Manual_Test import Ui_Dialog_Manual_Test


class ManualTestDlg(QDialog,Ui_Dialog_Manual_Test):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)


        self.pushButton_Measure.clicked.connect(self.fun_measure)


    def closewindow(self):
        self.close()

    def fun_measure(self):
        print("measure")