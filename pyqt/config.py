import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
#####---- connection----#####
def connection():
    db = mysql.connector.connect(user='root',password='',host='localhost',database='diction')
    db.set_charset_collation("utf8")
    return db
	######------ form show ---- #######
def formShow(self,ui_form):
	self.welcomeForm = QtWidgets.QMainWindow()
	self.ui = ui_form()
	self.ui.setupUi(self.welcomeForm)
	self.welcomeForm.show()
def showMessage(self,title,message,button,icon):
	msgBox = QtWidgets.QMessageBox()
	msgBox.setIcon(icon)
	msgBox.setWindowTitle(title)
	msgBox.setText(message)
	msgBox.setStandardButtons(button)
	msgBox.exec_()
def exitForm(self):
	exit()
# def loginCheck(self):
#         username = self.txt_user.text()
#         password = self.txt_pass.text()
#         #-connect-#
#         conn = connection()
#         cursor = conn.cursor()
#         sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
#         result = cursor.execute(sql)
#         data = cursor.fetchall()
#         if len(data) > 0:
#         	print("OK")
#         	formShow(self,Ui_welcomeForm)
#         else:
#         	print("USERNAME OR PASSWORD wrong")
# def signupCheck(self,signup):
#     username = self.txt_user.text()
#     password = self.txt_pass.text()
#     repass   = self.txt_repass.text()
#     #-connect-#
#     if (str(username) == "") | (str(password) == "") | (str(repass) == ""):
#         showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
#     else:
#         conn = connection()
#         cursor = conn.cursor()
#         sql = "SELECT * FROM user WHERE username = '" + username + "'"
#         result = cursor.execute(sql)
#         data = cursor.fetchall()
#         if password != repass:
#             showMessage(self,"Error","Repassword wrong",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
#         elif len(data) > 0:
#             showMessage(self,"Error","USERNAME exists",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
#         else:
#             sqlInsert = "INSERT INTO user(username,password) VALUES('" + username + "','" + password + "')"
#             try:
#                 signupAcc = cursor.execute(sqlInsert)
#                 conn.commit()
#                 showMessage(self,"Success","Signup Success",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
#                 signup.setEnabled(False)
#             except Exception as e:
#                 conn.rollback()
#             conn.close()