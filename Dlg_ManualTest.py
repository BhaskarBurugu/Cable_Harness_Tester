import socket
from time import sleep

import nidmm
from PyQt5.QtWidgets import QDialog, QMessageBox

from Ui_Manual_Test import Ui_Dialog_Manual_Test


class ManualTestDlg(QDialog,Ui_Dialog_Manual_Test):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)

        #self.lineEdit_VFDMM.setInputMask("00000.00")
        self.pushButton_Measure.clicked.connect(self.fun_measure)
        for i in range(1,129):
            self.comboBox_line1.addItem("PIN-"+str(i))
            self.comboBox_Line2.addItem("PIN-"+str(i))

    def closewindow(self):
        self.close()

    def fun_measure(self):
        print("measure")

        try:
            self.sock = socket.socket()
            self.sock.connect(('192.168.1.10', 5003))
        except:
            print('unable to connect to server')
            QMessageBox.information(self, "Link Down", "Unable to Communicate with  Interface Box")
            return 
        try:
            self.session = nidmm.Session("DMM4605")
            self.session.configure_measurement_digits(measurement_function=nidmm.Function["TWO_WIRE_RES"], range=10e3,
                                                 resolution_digits=6.5)
        except:
            QMessageBox.information(self, "Link Down", "Unable to Communicate with  DMM")
            return

        lineX = int(self.comboBox_line1.currentText()[4:])
        lineY = int(self.comboBox_Line2.currentText()[4:])

        Packet = []
        Packet.append(0xCC)
        Packet.append(lineX) #lineX
        Packet.append(0x01)
        Packet.append(lineY) #lineY
        Packet.append(0x01)
        try:
            self.sock.send(bytes(Packet))
            sleep(0.3)
        except:
            print('Tansmission Failed')
            # QMessageBox.information(self, "Communication Link Down", "Unable to Communicate with  Hardware")
            msg = QMessageBox.critical(self, "Link Down",
                                       "Unable to Communicate with Interface Box\nDo you want to Retry?",
                                       QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.Yes:
                QMessageBox.information(self, "Link Down",
                                        "Restart Interface Box\nWait till LAN LEDs Blinking on front Panel")
                self.sock.close()
                try:
                    self.sock = socket.socket()
                    self.sock.connect(('192.168.1.10', 5003))
                except:
                    print('unable to connect to server')
                    QMessageBox.information(self, "Communication Link Down",
                                            "Unable to Communicate with  Interface Box")
                    return

        measured_value = self.GetMeasfromDMM(session=self.session, range=100e3)
        if measured_value == None:
            QMessageBox.critical(self, "Link Down", "Unable to Communicate with  DMM")
            return
        self.lineEdit_VFDMM.setText(f'''{measured_value:.2f}''')
        print(measured_value)

    #################################################################################################################
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