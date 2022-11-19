import datetime
import math
import socket
from time import sleep

import nidmm
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, qApp, QHeaderView
from openpyxl import load_workbook
from openpyxl.styles import Side, Border

from Ui_Pin_to_Pin_Manual import Ui_Dialog_Pin_to_PinManual
from Reports_Generator import Get_Reports
from Dlg_FaultReport import FaultReportDlg


class Pin_to_Pin_ManualDlg(QDialog,Ui_Dialog_Pin_to_PinManual):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.tableWidget.setRowCount(128)
        self.min=0
        self.max=5
        self.AbortTestFlag = False
        self.TestFailFlag = False
        self.FaultReportDlg = FaultReportDlg()
        self.FaultReportDlg.tableWidget.setRowCount(128)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_Back.clicked.connect(self.closewindow)

        self.pushButton_Measure.clicked.connect(self.fun_measure)
        self.pushButton_Abort.clicked.connect(self.AbortTest)
        #self.pushButton_Save.clicked.connect(self.SaveReport)
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
        msg = QMessageBox.critical(self,"Pin to Pin Manual","Do you want to Abort?",QMessageBox.Yes|QMessageBox.No)
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
    #################################################################################################
    def fun_measure(self):

        try:
            sock = socket.socket()
            sock.connect(('192.168.1.10', 5003))
        except:
            print('unable to connect to server')
            QMessageBox.information(self, "Link Down", "Unable to Communicate with  Interface Box")
            return
        try:
            session = nidmm.Session("DMM4065")
            session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=10e3,
                                                 resolution_digits=6.5)
        except:
            QMessageBox.information(self, "Link Down", "Unable to Communicate with  DMM")
            return
        lineX = int(self.comboBox_LineX.currentText()[4:])
        inputfrom = int(self.comboBox_From.currentIndex())
        inputto = int(self.comboBox_To.currentText()[4:])
        range_span = inputto - inputfrom + 1

        self.pushButton_Measure.setDisabled(True)
        self.pushButton_Abort.setEnabled(True)
        self.pushButton_Back.setDisabled(True)
        self.pushButton_Save.setDisabled(True)
        self.tableWidget.setRowCount(range_span-1)
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ["S.No", "Line X", "Linw Y", "Min", "Measured ", "Max", "Units", "Result"])
        self.AbortTestFlag = False
        measured_value = 4.5
        FailTrailCount = 0
        i = 0
        falutypoints = 0
        while (self.AbortTestFlag == False) and (i < range_span-1):
            lineY = i
            print(lineX,lineY)
            Packet = []
            Packet.append(0xCC)
            Packet.append(lineX)
            Packet.append(0x01)
            Packet.append(lineY+1)
            Packet.append(0x01)
            if lineX in range(0, 64) and lineY in range(0, 64):
                print('Specs 0 to 10 Ohm')
                self.min = 0
                self.max = 10
            elif lineX in range(0, 64) and lineY in range(64, 128):
                print('Spec > 1K Ohm')
                self.min = 950
                self.max = 1050
            elif lineX in range(64, 128) and lineY in range(0, 64):
                print('Spec > 1K Ohm')
                self.min = 950
                self.max = 1050
            elif lineX in range(64, 128) and lineY in range(64, 128):
                print('Specs 0 to 10 Ohm')
                self.min = 0
                self.max = 10
            try:
                sock.send(bytes(Packet))
                sleep(0.1)
            except:
                print('Tansmission Failed')
                # QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
                msg = QMessageBox.critical(self, "Link Down", "Unable to Communicate with Interface Box\nDo you want to Retry?",
                                           QMessageBox.Yes | QMessageBox.No)
                if msg == QMessageBox.Yes:
                    QMessageBox.information(self, "Link Down",
                                            "Restart Interface Box\nWait till LAN LEDs Blinking on front Panel")
                    sock.close()
                    try:
                        sock = socket.socket()
                        sock.connect(('192.168.1.10', 5003))
                    except:
                        print('unable to connect to server')
                        QMessageBox.information(self, "Communication Link Down",
                                                "Unable to Communicate with  Interface Box")
                        return
                else:
                    self.AbortTestFlag = True
                    sock.close()

            self.tableWidget.setItem(i,0,QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i,1,QTableWidgetItem("PIN-"+str(lineX)))
            self.tableWidget.setItem(i,2,QTableWidgetItem("PIN-"+str(i+1)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.min)))

            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.max)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))

            self.tableWidget.selectRow(i)
            self.progressBar.setValue(int((i+1)*100/range_span))

            qApp.processEvents()
            measured_value = self.GetMeasfromDMM(session=session,range=100e3)

            if measured_value == None:
                msg = QMessageBox.critical(self, "Link Down", "Unable to Communicate with  DMM\nDo you want to Retry?",
                                           QMessageBox.Yes | QMessageBox.No)
                if msg == QMessageBox.Yes:
                    QMessageBox.information(self, "Link Down",
                                            "Unplug USB Cable of DMM & re-plug. wait for few seconds")
                    try:
                        session = nidmm.Session("DMM4065")
                        session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"],
                                                             range=10e3,
                                                             resolution_digits=6.5)
                    except:
                        #QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
                        return
                else:
                    self.AbortTestFlag = True
                    self.tableWidget.setRowCount(self.tableWidget.currentRow()+1)
            else:
                if measured_value == 20e6:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem('20M Ohm'))
                else:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(f'''{measured_value:.2f}'''))
                if measured_value>=self.min and measured_value<=self.max:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("PASS"))
                    qApp.processEvents()
                    i = i + 1
                    FailTrailCount = 0
                elif FailTrailCount >=3:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
                    self.FaultReportDlg.tableWidget.setRowCount(falutypoints+1)
                    self.FaultReportDlg.label.setText("SELF TEST-FAULTS REPORT")
                    self.FaultReportDlg.GUI="SelfTest"

                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 0, QTableWidgetItem(self.tableWidget.item(i,0).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 1, QTableWidgetItem(self.tableWidget.item(i,1).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 2, QTableWidgetItem(self.tableWidget.item(i,2).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 3, QTableWidgetItem(self.tableWidget.item(i,3).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 4, QTableWidgetItem(self.tableWidget.item(i,4).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 5, QTableWidgetItem(self.tableWidget.item(i,5).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 6, QTableWidgetItem(self.tableWidget.item(i,6).text()))
                    self.FaultReportDlg.tableWidget.setItem(falutypoints, 7, QTableWidgetItem(self.tableWidget.item(i,7).text()))
                    #self.FaultReportDlg.tableWidget.setItem(falutypoints, 0, self.tableWidget.item(i, 0).text())
                    falutypoints = falutypoints + 1
                    self.TestFailFlag=True
                    i = i + 1
                    FailTrailCount = 0
                else:
                    FailTrailCount  = FailTrailCount + 1
        sock.close()
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setEnabled(True)
        self.pushButton_Measure.setEnabled(True)
        print("measure")
        '''
        if self.TestFailFlag==True:
            self.TestFailFlag=False
            frmsg = QMessageBox.question(self,"Failure Report","Do you want to view the Failure Report",QMessageBox.Yes|QMessageBox.No)
            if frmsg==QMessageBox.Yes:
                dlg = self.FaultReportDlg
                dlg.exec()
        '''
    #################################################################################################################
    def GetMeasfromDMM(self, session=None, range=100e6):
        # with nidmm.Session("DMM4605") as session:
       # session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=range,
       #                                      resolution_digits=6.5)
        try:
            meas_res = session.read()
            if math. isnan(meas_res):
                meas_res = 20e6
            return meas_res
        except:
            print("out of range")
            #QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return None
    ##########################################################################################################
    def SaveReport(self):
        workbook = load_workbook(filename="Reports/PTPManual/PTPManualTemplate.xlsx")
        # open workbook
        sheet = workbook.active

        for i in range(0, self.tableWidget.rowCount()):
            sheet[f'''A{i + 8}'''] = self.tableWidget.item(i, 0).text()
            sheet[f'''B{i + 8}'''] = self.tableWidget.item(i, 1).text()
            sheet[f'''C{i + 8}'''] = self.tableWidget.item(i, 2).text()
            sheet[f'''D{i + 8}'''] = self.tableWidget.item(i, 3).text()
            sheet[f'''E{i + 8}'''] = self.tableWidget.item(i, 4).text()
            sheet[f'''F{i + 8}'''] = self.tableWidget.item(i, 5).text()
            sheet[f'''G{i + 8}'''] = self.tableWidget.item(i, 6).text()
            sheet[f'''H{i + 8}'''] = self.tableWidget.item(i, 7).text()

        self.set_border(sheet, f'''A8:H{8 + i}''')

        # save the file
        outfile = "Reports/PTPManual/PTPManual" + datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S') + '.xlsx'
        workbook.save(filename=outfile)
        QMessageBox.information(self, "Pin To Pin Manual Test", "Reports Saved to " + outfile)

    #################################################################################################################
    def set_border(self, worksheet, cell_range):
        thin = Side(border_style="thin", color="000000")
        for row in worksheet[cell_range]:
            for cell in row:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    def changeindex(self):
        index = self.comboBox_From.currentIndex()
        self.comboBox_To.clear()
        for i in range(index,128):
            self.comboBox_To.addItem("PIN-"+str(i+1))