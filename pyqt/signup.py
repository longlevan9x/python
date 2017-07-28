# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import mysql.connector
from home import Ui_home
from PyQt5 import QtCore, QtGui, QtWidgets
from config import *
import sys
class Ui_signup(object):
    def loginShow(self):
        from login import Ui_login
        formShow(self,Ui_login)
    def exitCheck(self):
        exitForm(self)
    def signupCheck(self):
        username = self.txt_user.text()
        password = self.txt_pass.text()
        repass   = self.txt_repass.text()
        #-connect-#
        if (str(username) == "") | (str(password) == "") | (str(repass) == ""):
            showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
        else:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM user WHERE username = '" + username + "'"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            if password != repass:
                showMessage(self,"Error","Repassword wrong",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
            elif len(data) > 0:
                showMessage(self,"Error","USERNAME exists",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
            else:
                sqlInsert = "INSERT INTO user(username,password) VALUES('" + username + "','" + password + "')"
                try:
                    signupAcc = cursor.execute(sqlInsert)
                    conn.commit()
                    showMessage(self,"Success","Signup Success. You login,please.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
                except Exception as e:
                    conn.rollback()
                conn.close()
    def setupUi(self, signup):
        signup.setObjectName("signup")
        signup.resize(431, 342)
        signup.setStyleSheet("QMainWindow{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 46, 90, 164), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.main_signup = QtWidgets.QWidget(signup)
        self.main_signup.setStyleSheet("")
        self.main_signup.setObjectName("main_signup")
        self.label = QtWidgets.QLabel(self.main_signup)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 61))
        self.label.setObjectName("label")
        self.lb_user = QtWidgets.QLabel(self.main_signup)
        self.lb_user.setGeometry(QtCore.QRect(70, 110, 71, 16))
        self.lb_user.setObjectName("lb_user")
        self.lb_pass = QtWidgets.QLabel(self.main_signup)
        self.lb_pass.setGeometry(QtCore.QRect(70, 150, 81, 16))
        self.lb_pass.setObjectName("lb_pass")
        self.lb_repass = QtWidgets.QLabel(self.main_signup)
        self.lb_repass.setGeometry(QtCore.QRect(70, 190, 91, 16))
        self.lb_repass.setObjectName("lb_repass")
        self.txt_user = QtWidgets.QLineEdit(self.main_signup)
        self.txt_user.setGeometry(QtCore.QRect(160, 110, 191, 20))
        self.txt_user.setObjectName("txt_user")
        self.txt_pass = QtWidgets.QLineEdit(self.main_signup)
        self.txt_pass.setGeometry(QtCore.QRect(160, 150, 191, 20))
        self.txt_pass.setMaxLength(50)
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setObjectName("txt_pass")
        self.txt_repass = QtWidgets.QLineEdit(self.main_signup)
        self.txt_repass.setGeometry(QtCore.QRect(160, 190, 191, 20))
        self.txt_repass.setMaxLength(50)
        self.txt_repass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_repass.setObjectName("txt_repass")
        self.btn_signup = QtWidgets.QPushButton(self.main_signup)
        self.btn_signup.setGeometry(QtCore.QRect(65, 240, 75, 23))
        self.btn_signup.setObjectName("btn_signup")
        ######## btn signup event click ########
        self.btn_signup.clicked.connect(self.signupCheck)
        # ###########################
        # self.btn_login = QtWidgets.QPushButton(self.main_signup)
        # self.btn_login.setGeometry(QtCore.QRect(160, 240, 75, 23))
        # self.btn_login.setObjectName("btn_login")
        # ######## btn login event click ########
        # self.btn_login.clicked.connect(self.loginShow)
        # ###########################
        self.btn_exit = QtWidgets.QPushButton(self.main_signup)
        self.btn_exit.setGeometry(QtCore.QRect(276, 240, 75, 23))
        self.btn_exit.setStyleSheet("")
        self.btn_exit.setObjectName("btn_exit")
        ######## btn exit event click ########
        self.btn_exit.clicked.connect(self.exitCheck)
        ###########################
        signup.setCentralWidget(self.main_signup)

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "Signup"))
        self.label.setText(_translate("signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Signup</span></p></body></html>"))
        self.lb_user.setText(_translate("signup", "USERNAME"))
        self.lb_pass.setText(_translate("signup", "PASSWORD"))
        self.lb_repass.setText(_translate("signup", "Re PASSWORD"))
        self.btn_signup.setText(_translate("signup", "Signup"))
        # self.btn_login.setText(_translate("signup", "Login"))
        self.btn_exit.setText(_translate("signup", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup = QtWidgets.QMainWindow()
    ui = Ui_signup()
    ui.setupUi(signup)
    signup.show()
    sys.exit(app.exec_())