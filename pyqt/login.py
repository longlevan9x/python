# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import mysql.connector
from home import Ui_home
from signup import Ui_signup
from PyQt5 import QtCore, QtGui, QtWidgets
from config import *

class Ui_login(object):
	################## START ##########
	########--- login ------########
    def loginCheck(self):
        username = self.txt_user.text()
        password = self.txt_pass.text()
    	#-connect-#
        conn = connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
        result = cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) > 0:
        	showMessage(self,"Success","Login Success",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
        	formShow(self,Ui_home)
        	login.hide()
        else:
        	showMessage(self,"Error","USERNAME OR PASSWORD Wrong",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
    #######- signup - #######
    def signupCheck(self):
        formShow(self,Ui_signup)
        self.btn_signup.setEnabled(False)
        self.btn_login.setEnabled(False)
    #######- Exit - #######
    def exitCheck(self):
    	exitForm(self)
    #################### END ##############

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        login.setEnabled(True)
        login.setStyleSheet("QDialog{\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 47, 216, 205), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_login = QtWidgets.QPushButton(login)
        self.btn_login.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.btn_login.setObjectName("btn_login")
        ##### event click button ###
        self.btn_login.clicked.connect(self.loginCheck)
        ######
        self.lb_user = QtWidgets.QLabel(login)
        self.lb_user.setGeometry(QtCore.QRect(80, 90, 71, 20))
        self.lb_user.setObjectName("lb_user")
        self.lb_pass = QtWidgets.QLabel(login)
        self.lb_pass.setGeometry(QtCore.QRect(80, 130, 71, 20))
        self.lb_pass.setObjectName("lb_pass")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 121, 41))
        self.label_3.setObjectName("label_3")
        self.txt_user = QtWidgets.QLineEdit(login)
        self.txt_user.setGeometry(QtCore.QRect(170, 90, 161, 20))
        self.txt_user.setObjectName("txt_user")
        self.txt_pass = QtWidgets.QLineEdit(login)
        self.txt_pass.setGeometry(QtCore.QRect(170, 130, 161, 20))
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setPlaceholderText("")
        self.txt_pass.setObjectName("txt_pass")
        self.btn_signup = QtWidgets.QPushButton(login)
        self.btn_signup.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.btn_signup.setObjectName("btn_signup")
        ######## btn signup event click ########
        self.btn_signup.clicked.connect(self.signupCheck)
        ###########################
        self.btn_exit = QtWidgets.QPushButton(login)
        self.btn_exit.setGeometry(QtCore.QRect(260, 190, 75, 23))
        self.btn_exit.setObjectName("btn_exit")
        ######## btn exit event click ########
        self.btn_exit.clicked.connect(self.exitCheck)
        ###########################
        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.btn_login.setText(_translate("login", "LOGIN"))
        self.lb_user.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:10pt;\">USERNAME</span></p></body></html>"))
        self.lb_pass.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:10pt;\">PASSWORD</span></p></body></html>"))
        self.label_3.setText(_translate("login", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">LOGIN</span></p></body></html>"))
        self.btn_signup.setText(_translate("login", "Signup"))
        self.btn_exit.setText(_translate("login", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
