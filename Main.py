
##########################################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView, QTableWidgetItem, QMessageBox, qApp

from Dlg_BrowseTest import BrowseTestDlg
from Dlg_DiodeTest import DiodeTestDlg
from Dlg_LoginScreen import LoginDlg
from Dlg_ManualTest import ManualTestDlg
from Dlg_PintoPinAutomatic import Pin_to_Pin_AutomaticDlg
from Ui_Main_Screen import Ui_MainWindow
from Dlg_PintoPinManual import Pin_to_Pin_ManualDlg
from Dlg_SelfTest import SelfTestDlg
###########################################################################################################
class CableHarnessTester(Ui_MainWindow):
    def __init__(self):
        self.global_var_1 = 1
        self.global_var_2 =2
        #self.setupUi(QMainWindow())
        #self.pushButton.clicked.connect(self.func_1)

    def func_1(self):
        print('Hello')

    def Slots_and_Signals(self):
        print('func_2')
        self.actionSelf_Test.triggered.connect(self.SelfTest)
        self.actionDiode_Test.triggered.connect(self.DiodeTest)
        self.actionPin_to_Pin_Automatic.triggered.connect(self.Pin_to_Pin_Auto)
        self.actionPin_to_Pin_Manual.triggered.connect(self.Pin_to_Pin_Manual)
        self.actionBrowse_Test.triggered.connect(self.Browse_Test)
        self.actionManual_Test.triggered.connect(self.Manual_Test)

        self.pushButton_SelfTest.clicked.connect(self.SelfTest)
        self.pushButton_DiodeTest.clicked.connect(self.DiodeTest)
        self.pushButton_PTPAut.clicked.connect(self.Pin_to_Pin_Auto)
        self.pushButton_PTPMan.clicked.connect(self.Pin_to_Pin_Manual)
        self.pushButton_BrowseTest.clicked.connect(self.Browse_Test)
        self.pushButton_ManualTest.clicked.connect(self.Manual_Test)

    def Login(self):
        print('Login')
        dlg = LoginDlg()
        dlg.exec()
        return dlg.validcred

    def SelfTest(self):
        print('SelfTest')
        dlg = SelfTestDlg()
        dlg.exec()
        #return dlg.validcred

    def DiodeTest(self):
        print('DiodeTest')
        dlg = DiodeTestDlg()
        dlg.exec()

    def Pin_to_Pin_Auto(self):
        print('Pin to Pin Automatic')
        dlg = Pin_to_Pin_AutomaticDlg()
        dlg.exec()

    def Pin_to_Pin_Manual(self):
        print('Pin to Pin Manual')
        dlg = Pin_to_Pin_ManualDlg()
        dlg.exec()

    def Browse_Test(self):
        print('Browse Test')
        dlg = BrowseTestDlg()
        dlg.exec()

    def Manual_Test(self):
        print('Manual Test')
        dlg = ManualTestDlg()
        dlg.exec()
###########################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create a main window
    main = QMainWindow()
 #   main.setFixedSize(500, 320)

    main_win = CableHarnessTester()
    main_win.setupUi(main)
    validatecredential = main_win.Login()
    if validatecredential == True:
        main_win.Slots_and_Signals()
        main.show()
        sys.exit(app.exec_())