import datetime
import socket
from time import sleep

import nidmm
from PyQt5.QtWidgets import *
from openpyxl import load_workbook
from openpyxl.styles import Side, Border

from Reports_Generator import Get_Reports
from Ui_Browse_Test import Ui_Dialog_BrowseTest

import os
####################################################################################################################
class BrowseTestDlg(QDialog,Ui_Dialog_BrowseTest):
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
        self.pushButton_Measure.setDisabled(True)


        self.progressBar.setValue(0)

        self.pushButton_Browse.clicked.connect(self.fun_browse)

        self.progressBar.setValue(0)

    def closewindow(self):
        self.close()
    #################################################################################################################
    def AbortTest(self):
        msg = QMessageBox.critical(self,"","Do you want to continue",QMessageBox.Yes|QMessageBox.No)
        if msg==QMessageBox.Yes:
            self.AbortTestFlag = True
            # This line removed by Bhaskar Rao on 10 Nov 2022
            #self.tableWidget.setRowCount(self.tableWidget.currentRow()+1)
            self.pushButton_Back.setEnabled(True)
            self.pushButton_Save.setEnabled(True)
            self.pushButton_Measure.setEnabled(True)
        else:
            self.AbortTestFlag = False
            self.pushButton_Back.setDisabled(True)
            self.pushButton_Save.setDisabled(True)
            self.pushButton_Measure.setDisabled(True)
    ###################################################################################################################
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
        self.AbortTestFlag = False
        measured_value = 4.5
        FailTrailCount = 0
        frominlist_byte = bytearray(self.frompinlist)
        topinlist_byte = bytearray(self.topinlist)
        #print(type(frominlist_byte[1]))
        for i in range(0,self.nr):
            self.tableWidget.setItem(i, 4, QTableWidgetItem('---'))
            self.tableWidget.setItem(i, 7, QTableWidgetItem("---"))
        i = 0
        while (self.AbortTestFlag == False) and (i < self.nr-8):
            Packet = []
            Packet.append(0xCC)
            Packet.append(frominlist_byte[i])
            print('Lane_X',frominlist_byte[i])
            Packet.append(0x01)
            Packet.append(topinlist_byte[i])
            print('Lane_Y', topinlist_byte[i])
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
                        #ComErrFlag = True
                    except:
                        print('unable to connect to server')
                        QMessageBox.information(self, "Communication Link Down",
                                                "Unable to Communicate with  Hardware")
                        return
                else:
                    self.AbortTestFlag = True
                    sock.close()

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem("PIN-" + str(frominlist_byte[i])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem("PIN-" + str(topinlist_byte[i])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.min)))

            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.max)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))

            self.tableWidget.setRowCount(self.nr)
            self.tableWidget.selectRow(i)
            self.progressBar.setValue(int((i + 1) * 100 / self.nr))

            qApp.processEvents()
            measured_value = self.GetMeasfromDMM(session=session, range=10e3)
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
                        ComErrFlag = True
                    except:
                        QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
                        return
                else:
                    self.AbortTestFlag = True
                '''
                if FailTrailCount >= 3:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str('>100K')))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
                    FailTrailCount = FailTrailCount + 1
                '''
            else:
                self.tableWidget.setItem(i, 4, QTableWidgetItem(f'''{measured_value:.2f}'''))
                if measured_value > self.min and measured_value < self.max:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("PASS"))
                    i = i + 1
                    FailTrailCount = 0
                elif FailTrailCount >= 3:
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("FAILED"))
                    i = i + 1
                    FailTrailCount = 0
                else:
                    FailTrailCount = FailTrailCount + 1
        sock.close()
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Abort.setDisabled(True)
        self.pushButton_Save.setEnabled(True)
        print("measure")

    def GetMeasfromDMM(self,session =None,range = 100e6):
        #with nidmm.Session("DMM4605") as session:

        try:
            meas_res = session.read()
            return meas_res
        except:
            print("out of range")
            QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  DMM")
            return None
    #################################################################################################################
    def fun_browse(self):
        path = QFileDialog.getOpenFileName(self, "Select File", os.getenv("Home"))
        if len(path) > 0:
            try:
                self.lineEdit.setText(path[0])
                self.frompinlist = []
                self.topinlist = []
                minvallist = []
                maxvallist = []
                workbook = load_workbook(filename=path[0])
                sheet = workbook.active
                self.nr = sheet.max_row
                for i in range(8, self.nr):
                    self.frompinlist.append(sheet.cell(i, 1).value)
                    self.topinlist.append(sheet.cell(i,3).value)
                    minvallist.append(sheet.cell(i,6).value)
                    maxvallist.append(sheet.cell(i, 7).value)
                self.tableWidget.setRowCount(self.nr-8)
                for i in range(0,self.nr-8):
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem("PIN-" + str(self.frompinlist[i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem("PIN-" + str(self.topinlist[i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(minvallist[i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem("---"))

                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(maxvallist[i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem("Ohms"))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem("---"))
                    self.pushButton_Measure.setDisabled(False)

            except:
                self.lineEdit.clear()
                self.tableWidget.clear()
                self.tableWidget.setRowCount(0)
                self.tableWidget.setHorizontalHeaderLabels(["S.No","Line X","Linw Y","Min","Measured Value","Max","Units","Result"])
                self.pushButton_Measure.setDisabled(True)
                QMessageBox.warning(self,"WARNING!!!","Invalid File Passed")
    ##########################################################################################################
    def SaveReport(self):
        # load excel file
        workbook = load_workbook(filename="Reports/BrowseTest/BrowseTestTemplate.xlsx")
        # open workbook
        sheet = workbook.active

        for i in range(0, self.nr-8):
            sheet[f'''A{i + 8}'''] = self.tableWidget.item(i, 0).text()
            sheet[f'''B{i + 8}'''] = self.tableWidget.item(i, 1).text()
            sheet[f'''C{i + 8}'''] = self.tableWidget.item(i, 2).text()
            sheet[f'''D{i + 8}'''] = self.tableWidget.item(i, 3).text()
            sheet[f'''E{i + 8}'''] = self.tableWidget.item(i, 4).text()
            sheet[f'''F{i + 8}'''] = self.tableWidget.item(i, 5).text()
            sheet[f'''G{i + 8}'''] = self.tableWidget.item(i, 6).text()
            sheet[f'''H{i + 8}'''] = self.tableWidget.item(i, 7).text()

        self.set_border(sheet, f'''A8:H{self.nr-1}''')

        # save the file
        workbook.save(
            filename="Reports/BrowseTest/BrowseTest" + datetime.datetime.now().strftime(
                '%d_%m_%Y_%H_%M_%S') + '.xlsx')
    #################################################################################################################
    def set_border(self,worksheet, cell_range):
        thin = Side(border_style="thin", color="000000")
        for row in worksheet[cell_range]:
            for cell in row:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)