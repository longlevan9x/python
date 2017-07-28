# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from config import *

class Ui_home(object):
    ######## ADD
    def addWord(self):
        word = self.txt_word.text()
        mean = self.txt_mean.text()
        if (word == "") | (mean == ""):
            showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
        else:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM dictionary WHERE word = N'" + word + "'"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) > 0:
                showMessage(self,"Error","Word exists. Add fail.",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Information)
            else:
                sqlInsert = "INSERT INTO dictionary(word,mean) VALUES('" + word + "','" + mean + "')"
                try:
                    add_word = cursor.execute(sqlInsert)
                    conn.commit()
                    showMessage(self,"Success","Add Success.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
                except Exception as e:
                    conn.rollback()
                conn.close()
    ######## SEARCH
    def searchWord(self):
        word = self.txt_words.text()
        if word == "":
            showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
        else:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM dictionary WHERE word = N'" + word + "'"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) > 0:
                for a in data:
                    self.txt_means.setText(a[1])
            else:
                self.txt_means.setText("")
    ########### UPDATE
    def updateWord(self):
        word = self.txt_words.text()
        mean = self.txt_means.text()
        if (word == "") | (mean == "") :
            showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
        else:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM dictionary WHERE word = N'" + word + "'"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) >= 1:
                sqlUpdate = "UPDATE dictionary SET mean = N'" + mean + "' WHERE word = '" + word + "'"
                try:
                    edit_word = cursor.execute(sqlUpdate)
                    conn.commit()
                    showMessage(self,"Success","Edit Success.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
                except Exception as e:
                    conn.rollback()
                conn.close()
            else:
                showMessage(self,"Error","Word not exists.Update fail.",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Information)
    ############ DELETE
    def deleteWord(self):
        word = self.txt_words.text()
        if word == "":
            showMessage(self,"Empty","The value not empty",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Critical)
        else:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM dictionary WHERE word = N'" + word + "'"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) > 0:
                sqlDelete = "DELETE FROM dictionary WHERE word = '" + word + "'"
                try:
                    delete_word = cursor.execute(sqlDelete)
                    conn.commit()
                    showMessage(self,"Success","Delete Success.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Information)
                except Exception as e:
                    conn.rollback()
                    self.txt_means.setText("")
                conn.close()
            else:
                showMessage(self,"Error","Word not exists. Delete fail.",QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Information)
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(584, 428)
        home.setMaximumSize(QtCore.QSize(584, 530))
        home.setSizeIncrement(QtCore.QSize(0, 0))
        home.setBaseSize(QtCore.QSize(0, 0))
        home.setStyleSheet("QMainWindow{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.352, y1:0.301136, x2:1, y2:1, stop:0.340909 rgba(230, 153, 126, 205), stop:0.909091 rgba(255, 255, 255, 255));\n"
"}")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        # self.btn_game = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_game.setGeometry(QtCore.QRect(30, 10, 75, 23))
        # self.btn_game.setObjectName("btn_game")
        self.btn_addword = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addword.setGeometry(QtCore.QRect(387, 100, 80, 25))
        self.btn_addword.setObjectName("btn_addword")
        ###########- add event
        self.btn_addword.clicked.connect(self.addWord)
        #############
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 105, 51, 20))
        self.label.setObjectName("label")
        self.txt_word = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_word.setGeometry(QtCore.QRect(150, 100, 215, 25))
        self.txt_word.setObjectName("txt_word")
        self.txt_word.setFont(font)
        self.lb_mean = QtWidgets.QLabel(self.centralwidget)
        self.lb_mean.setGeometry(QtCore.QRect(80, 145, 47, 13))
        self.lb_mean.setObjectName("lb_mean")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 190, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 255, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 305, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 265, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txt_words = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_words.setGeometry(QtCore.QRect(150, 260, 215, 25))
        self.txt_words.setFont(font)
        self.txt_words.setObjectName("txt_words")
        self.btn_searchw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_searchw.setGeometry(QtCore.QRect(387, 260, 80, 25))
        self.btn_searchw.setObjectName("btn_searchw")
        ###########- search event
        self.btn_searchw.clicked.connect(self.searchWord)
        #############---
        self.btn_updatew = QtWidgets.QPushButton(self.centralwidget)
        self.btn_updatew.setGeometry(QtCore.QRect(170, 340, 80, 25))
        self.btn_updatew.setObjectName("btn_updatew")
        ###########- delete event
        self.btn_updatew.clicked.connect(self.updateWord)
        #############---
        self.btn_deletew = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deletew.setGeometry(QtCore.QRect(290, 340, 80, 25))
        self.btn_deletew.setObjectName("btn_deletew")
        ###########- delete event
        self.btn_deletew.clicked.connect(self.deleteWord)
        #############---
        self.txt_mean = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_mean.setGeometry(QtCore.QRect(150, 140, 315, 25))
        self.txt_mean.setFont(font)
        self.txt_mean.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_mean.setObjectName("txt_mean")
        self.txt_means = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_means.setGeometry(QtCore.QRect(150, 300, 315, 25))
        self.txt_means.setFont(font)
        self.txt_means.setObjectName("txt_means")
        home.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.txt_word)
        self.label_2.setBuddy(self.txt_words)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)
        home.setTabOrder(self.txt_word, self.txt_mean)
        home.setTabOrder(self.txt_mean, self.btn_addword)
        home.setTabOrder(self.btn_addword, self.txt_words)
        home.setTabOrder(self.txt_words, self.txt_means)
        home.setTabOrder(self.txt_means, self.btn_searchw)
        # home.setTabOrder(self.btn_searchw, self.btn_game)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Home"))
        # self.btn_game.setText(_translate("home", "Game"))
        self.btn_addword.setText(_translate("home", "Add word"))
        self.label.setText(_translate("home", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Word</span></p></body></html>"))
        self.lb_mean.setText(_translate("home", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Mean</span></p></body></html>"))
        self.label_3.setText(_translate("home", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Dictionary Anh - Viet</span></p></body></html>"))
        self.label_4.setText(_translate("home", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Mean</span></p></body></html>"))
        self.label_2.setText(_translate("home", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Word</span></p></body></html>"))
        self.btn_searchw.setText(_translate("home", "Search Word"))
        self.btn_deletew.setText(_translate("home", "Delete Word"))
        self.btn_updatew.setText(_translate("home", "Edit Word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())

