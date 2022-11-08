import json

from PyQt5.QtWidgets import QDialog
from Ui_Login import Ui_Login_Screen

class LoginDlg(QDialog,Ui_Login_Screen):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.validcred = False
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.validatecredentials)

    def validatecredentials(self):
        print('Validate Credentials')
        # Opening JSON file
        with open('logincred.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        for username, password in json_object.items():
            if (username == self.lineEdit_Username.text()) and (password == self.lineEdit_Password.text()):
                self.validcred = True
                self.close()