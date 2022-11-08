import datetime
import socket
import sys
from time import sleep

from PyQt5.QtWidgets import *#QDialog, QHeaderView
import pyvisa
import nidmm


from Reports_Generator import Get_Reports
from Ui_SelfTest import Ui_Dialog_SelfTest

#################################################################################################################
class SelfTestDlg(QDialog,Ui_Dialog_SelfTest):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.AbortTestFlag = False
        self.min = 0
        self.max = 5
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)

        self.pushButton_Measure.clicked.connect(self.fun_measure)
        self.pushButton_Abort.clicked.connect(self.AbortTest)
        self.pushButton_Save.clicked.connect(self.SaveReport)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setDisabled(True)

        self.progressBar.setValue(0)
    ################################################################################################################
    def closewindow(self):
        self.close()
    ################################################################################################################
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
    #################################################################################################################
    def fun_measure(self):
        i = 0
        try:
            sock = socket.socket()
            sock.connect(('192.168.1.10', 5003))
        except:
            print('unable to connect to server')
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
            return
        try:
            session = nidmm.Session("DMM4605")
        except:
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return

        self.pushButton_Abort.setEnabled(True)
        self.pushButton_Back.setDisabled(True)
        self.pushButton_Save.setDisabled(True)
        self.tableWidget.setRowCount(0)
        self.AbortTestFlag = False
        measured_value = 4.5
        self.tableWidget.setRowCount(128)
        FailTrailCount = 0
        while (self.AbortTestFlag == False) and (i<128) :
            Packet = []
            Packet.append(0xCC)
            Packet.append(i+1)
            Packet.append(0x01)
            Packet.append(i+1)
            Packet.append(0x01)
            try:
                sock.send(bytes(Packet))
                sleep(0.01)
            except:
                print('Tansmission Failed')
                QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
                sock.close()
                self.AbortTestFlag = True
                #return

            self.tableWidget.setItem(i,0,QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i,1,QTableWidgetItem("PIN-"+str(i+1)))
            self.tableWidget.setItem(i,2,QTableWidgetItem("PIN-"+str(i+1)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.min)))

            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.max)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))

            self.tableWidget.selectRow(i)
            self.progressBar.setValue(int((i+1)*100/128))

            qApp.processEvents()
            measured_value = self.GetMeasfromDMM(session=session,range=100e3)
            if measured_value == None :
                self.AbortTestFlag = True
                '''
                if FailTrailCount >= 3:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str('>100K')))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
                    FailTrailCount = FailTrailCount + 1
                '''
            else:
                self.tableWidget.setItem(i, 4, QTableWidgetItem(f'''{measured_value:.2f}'''))
                if measured_value>self.min and measured_value<self.max:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("PASS"))
                    i = i + 1
                    FailTrailCount = 0
                elif FailTrailCount >=3:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
                    i = i + 1
                    FailTrailCount = 0
                else:
                    FailTrailCount  = FailTrailCount + 1
        sock.close()
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setEnabled(True)
        print("measure")
    ###########################################################################################################
    def GetMeasfromDMM(self,session =None,range = 100e6):
        #with nidmm.Session("DMM4605") as session:

        session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=range,
                                                 resolution_digits=6.5)
        try:
            meas_res = session.read()
            return meas_res
        except:
            print("out of range")
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return None
    #############################################################################################################

    def SaveReport(self):
        Get_Reports().Generate_Report_SelfTest(self.tableWidget)