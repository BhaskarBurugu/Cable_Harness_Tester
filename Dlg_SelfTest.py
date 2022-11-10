import datetime
import socket
import sys
from time import sleep

from PyQt5.QtWidgets import *#QDialog, QHeaderView
import pyvisa
import nidmm
from openpyxl import load_workbook
from openpyxl.styles import Side, Border

from Reports_Generator import Get_Reports
from Ui_SelfTest import Ui_Dialog_SelfTest

#################################################################################################################
class SelfTestDlg(QDialog,Ui_Dialog_SelfTest):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.AbortTestFlag = False
        self.min = 0
        self.max =10
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
            self.pushButton_Measure.setEnabled(True)
        else:
            self.AbortTestFlag = False
            self.pushButton_Back.setDisabled(True)
            self.pushButton_Save.setDisabled(True)
            self.pushButton_Measure.setDisabled(True)
    #################################################################################################################
    def fun_measure(self):

        try:
            sock = socket.socket()
            sock.connect(('192.168.1.10', 5003))
        except:
            print('unable to connect to server')
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
            return
        try:
            session = nidmm.Session("DMM4605")
            session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=10e3,
                                                 resolution_digits=6.5)
        except:
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return
        self.pushButton_Measure.setDisabled(True)
        self.pushButton_Abort.setEnabled(True)
        self.pushButton_Back.setDisabled(True)
        self.pushButton_Save.setDisabled(True)
        self.tableWidget.setRowCount(0)
        self.AbortTestFlag = False
        measured_value = 4.5
        self.tableWidget.setRowCount(128)
        FailTrailCount = 0
        i = 0
        while (self.AbortTestFlag == False) and (i<128) :
            Packet = []
            Packet.append(0xCC)
            Packet.append(i+1)
            Packet.append(0x01)
            Packet.append(i+1)
            Packet.append(0x01)
            try:
                sock.send(bytes(Packet))
                sleep(0.1)
            except:
                print('Tansmission Failed')
                # QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
                msg = QMessageBox.critical(self, "Link Down", "Do you want to continue",
                                           QMessageBox.Yes | QMessageBox.No)
                if msg == QMessageBox.Yes:
                    QMessageBox.information(self, "Link Down",
                                            "Restart Hardware\nWait till LAN LEDs Blinking on front Panel")
                    sock.close()
                    try:
                        sock = socket.socket()
                        sock.connect(('192.168.1.10', 5003))
                    except:
                        print('unable to connect to server')
                        QMessageBox.information(self, "Communication Link Down",
                                                "Unable to Communicate with  Hardware")
                        return
                else:
                    self.AbortTestFlag = True
                    sock.close()

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
            if measured_value == None:
                msg = QMessageBox.critical(self, "Link Down", "Unable to Communicate with  DMM",
                                           QMessageBox.Yes | QMessageBox.No)
                if msg == QMessageBox.Yes:
                    QMessageBox.information(self, "Link Down",
                                            "Unplug USB Cable of DMM & re-plug. wait for few seconds")
                    try:
                        session = nidmm.Session("DMM4605")
                        session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"],
                                                             range=10e3,
                                                             resolution_digits=6.5)
                    except:
                        QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
                        return
                else:
                    self.AbortTestFlag = True
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

       # session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=range,
       #                                          resolution_digits=6.5)
        try:
            meas_res = session.read()
            return meas_res
        except:
            print("out of range")
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return None
    #############################################################################################################

    def SaveReport(self):
        workbook = load_workbook(filename="Reports/SelfTest/SelfTestTemplate.xlsx")
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

        self.set_border(sheet, f'''A8:H{8+i-1}''')

        # save the file
        workbook.save(filename="Reports/SelfTest/SelfTest"+datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')+'.xlsx')
    #################################################################################################################
    def set_border(self,worksheet, cell_range):
        thin = Side(border_style="thin", color="000000")
        for row in worksheet[cell_range]:
            for cell in row:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)