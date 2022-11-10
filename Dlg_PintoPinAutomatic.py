import socket
from math import nan
from time import sleep

import nidmm
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QHeaderView, QMessageBox, QTableWidgetItem, qApp

from Reports_Generator import Get_Reports
from Ui_SelfTest import Ui_Dialog_SelfTest


class Pin_to_Pin_AutomaticDlg(QDialog,Ui_Dialog_SelfTest):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setGeometry(QtCore.QRect(350, 20, 400, 31))
        self.setWindowTitle("Automatic Test")
        self.label.setText("PIN-PIN AUTOMATIC TEST ")
        self.AbortTestFlag = False
        self.min = 0
        self.max = 10
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
        msg = QMessageBox.critical(self, "", "Do you want to continue", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.AbortTestFlag = True
            self.tableWidget.setRowCount(self.tableWidget.currentRow() + 1)
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

        self.pushButton_Abort.setEnabled(True)
        self.pushButton_Back.setDisabled(True)
        self.pushButton_Save.setDisabled(True)
        self.pushButton_Measure.setDisabled(True)

        self.tableWidget.setRowCount(0)
        self.AbortTestFlag = False
        self.tableWidget.setRowCount(64*129)
        rowcount = 0
        for j in range(0,128):
            i = j
            while (self.AbortTestFlag == False) and (i < 128):
                ComErrFlag = False
                Packet = []
                Packet.append(0xCC)
                Packet.append(j + 1)
                Packet.append(0x01)
                Packet.append(i + 1)
                Packet.append(0x01)
                try:
                    sock.send(bytes(Packet))
                    if i ==j:
                        sleep(0.1)
                except:
                    print('Tansmission Failed')
                    #QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
                    msg = QMessageBox.critical(self, "Link Down", "Do you want to continue", QMessageBox.Yes | QMessageBox.No)
                    if msg == QMessageBox.Yes:
                        QMessageBox.information(self, "Link Down", "Restart Hardware\nWait till LAN LEDs Blinking on front Panel")
                        sock.close()
                        try:
                            sock = socket.socket()
                            sock.connect(('192.168.1.10', 5003))
                            ComErrFlag = True
                        except:
                            print('unable to connect to server')
                            QMessageBox.information(self, "Communication Link Down",
                                                    "Unable to Communicate with  Hardware")
                            return
                    else:
                        self.AbortTestFlag = True
                        sock.close()

                self.tableWidget.setItem(rowcount, 0, QTableWidgetItem(str(rowcount + 1)))
                self.tableWidget.setItem(rowcount, 1, QTableWidgetItem("PIN-" + str(j + 1)))
                self.tableWidget.setItem(rowcount, 2, QTableWidgetItem("PIN-" + str(i + 1)))

                self.tableWidget.setItem(rowcount, 6, QTableWidgetItem("Ohms"))

                self.tableWidget.selectRow(rowcount)
                self.progressBar.setValue(int((i+ 1) * 100 / 128))

                qApp.processEvents()
                sleep(0.1)
                measured_value = self.GetMeasfromDMM(session=session, range=10e3)
                if measured_value == None:
                    msg = QMessageBox.critical(self, "Link Down", "Unable to Communicate with  DMM", QMessageBox.Yes | QMessageBox.No)
                    if msg == QMessageBox.Yes:
                        QMessageBox.information(self, "Link Down", "Unplug USB Cable of DMM & re-plug. wait for few seconds")
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
                    self.tableWidget.setItem(rowcount, 4, QTableWidgetItem(f'''{measured_value:.2f}'''))
                    #self.tableWidget.setItem(i, 7, QTableWidgetItem("PASS"))
                    if i in range(0, 64) and j in range(0, 64):
                        print('Specs 0 to 10 Ohm')
                        self.min = 0
                        self.max = 10
                    elif i in range(0, 64) and j in range(64, 128):
                        print('Spec > 1K Ohm')
                        self.min = 950
                        self.max = 1050
                    elif i in range(64, 128) and j in range(0, 64):
                        print('Spec > 1K Ohm')
                        self.min = 950
                        self.max = 1050
                    elif i in range(64, 128) and j in range(64, 128):
                        print('Specs 0 to 10 Ohm')
                        self.min = 0
                        self.max = 10
                    self.tableWidget.setItem(rowcount, 3, QTableWidgetItem(str(self.min)))
                    self.tableWidget.setItem(rowcount, 5, QTableWidgetItem(str(self.max)))

                    if measured_value > self.min and measured_value < self.max:
                        self.tableWidget.setItem(rowcount, 7, QTableWidgetItem("PASS"))
                        i = i + 1
                        FailTrailCount = 0
                        rowcount = rowcount + 1
                    elif FailTrailCount >= 3:
                        self.tableWidget.setItem(rowcount, 7, QTableWidgetItem("FAILED"))
                        i = i + 1
                        FailTrailCount = 0
                        rowcount = rowcount + 1
                    else:
                        FailTrailCount = FailTrailCount + 1
                '''
                if ComErrFlag == False:
                    i = i + 1
                    rowcount = rowcount + 1
                '''

        sock.close()
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setEnabled(True)
        print("measure")

    ###########################################################################################################
    def GetMeasfromDMM(self, session=None, range=100e6):
        # with nidmm.Session("DMM4605") as session:
       # session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=range,
       #                                      resolution_digits=6.5)
        try:
            meas_res = session.read()
            return meas_res
        except:
            print("out of range")
            #QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return None

    #############################################################################################################
    def SaveReport(self):
        Get_Reports().Generate_Report_PTPAut(self.tableWidget)