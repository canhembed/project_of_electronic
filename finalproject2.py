# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apptest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt,QThread,QSize,pyqtSignal

import datetime
import time
import pygame

#import json
from firebase import firebase
#from firebase import jsonutil


class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(480,320))
        self.setWindowTitle("Family medicine Box")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTieuDe = QtWidgets.QLabel(self.centralwidget)
        self.lblTieuDe.setGeometry(QtCore.QRect(60, 10, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTieuDe.setFont(font)
        self.lblTieuDe.setStyleSheet("rgb(255, 0, 0)")
        self.lblTieuDe.setObjectName("lblTieuDe")
        
        self.btnGiupdo = QtWidgets.QPushButton(self.centralwidget)
        self.btnGiupdo.setGeometry(QtCore.QRect(0, 0, 61, 21))
        self.btnGiupdo.setObjectName("btnGiupdo")
        self.btnGiupdo.clicked.connect(self.LoadHelp)
        
        self.lblDonThuoc = QtWidgets.QLabel(self.centralwidget)
        self.lblDonThuoc.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDonThuoc.setFont(font)
        self.lblDonThuoc.setObjectName("lblDonThuoc")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 40, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        
        self.lblTenthuoc = QtWidgets.QLabel(self.centralwidget)
        self.lblTenthuoc.setGeometry(QtCore.QRect(40, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTenthuoc.setFont(font)
        self.lblTenthuoc.setObjectName("lblTenthuoc")
        self.lblLieuluong = QtWidgets.QLabel(self.centralwidget)
        self.lblLieuluong.setGeometry(QtCore.QRect(180, 60, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLieuluong.setFont(font)
        self.lblLieuluong.setObjectName("lblLieuluong")
        self.lblThoigian = QtWidgets.QLabel(self.centralwidget)
        self.lblThoigian.setGeometry(QtCore.QRect(270, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblThoigian.setFont(font)
        self.lblThoigian.setObjectName("lblThoigian")
        self.lblGhiChu = QtWidgets.QLabel(self.centralwidget)
        self.lblGhiChu.setGeometry(QtCore.QRect(380, 60, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblGhiChu.setFont(font)
        self.lblGhiChu.setObjectName("lblGhiChu")
        
        self.btnDaXem = QtWidgets.QPushButton(self.centralwidget)
        self.btnDaXem.setGeometry(QtCore.QRect(380, 240, 75, 31))
        self.btnDaXem.setObjectName("btnDaXem")

        self.btnThietlaplai = QtWidgets.QPushButton(self.centralwidget)
        self.btnThietlaplai.setGeometry(QtCore.QRect(270, 240, 75, 31))
        self.btnThietlaplai.setObjectName("btnThietlaplai")
       	
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 431, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1000)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)

        self.Load_Data_Hours()
        self.Load_dulieu_Firebase()
        self.btnGiupdo.clicked.connect(self.LoadHelp)
        self.btnDaXem.clicked.connect(self.LoadDaxem)
        self.btnThietlaplai.clicked.connect(self.LoadThietlaplai)


    def LoadDaxem(self):
    	global dx
    	dx=1
    	print("da xem dx=",dx)
    def LoadThietlaplai(self):
    	global dx
    	dx=0
    	print("thiet lap lại dx=",dx)
        
    def LoadHelp(self):
    	QMessageBox.information(self,'Help','Đây là ứng dụng Tủ thuốc gia đình: \n'+
    		'- Có chức năng nhắc nhở thời gian uống thuốc \n'+
    		'- Cũng như theo dõi đơn thuốc hàng ngày\n'+
    		"- Khi đã lấy thuốc thì vui lòng nhấn Đã xem\n"+
    		"- Thiết bị hoạt động ở điện áp 5VDC-2.5A\n"+
    		"  (vui lòng cấp đúng điện áp).\n",QMessageBox.Ok)

    def on_info_firebase(self,x):
    	global Row
    	self.tableWidget.setItem(Row,0, QTableWidgetItem(TenThuoc))
    	self.tableWidget.setItem(Row,1, QTableWidgetItem(LieuLuong))
    	self.tableWidget.setItem(Row,2, QTableWidgetItem(ThoiGian))
    	self.tableWidget.setItem(Row,3, QTableWidgetItem(GhiChu))
    	print(TenThuoc)
    	print(LieuLuong)
    	print(ThoiGian)
    	print(GhiChu)

    def Load_dulieu_Firebase(self):
    	#global x
    	#global TenThuoc
    	#global LieuLuong
    	#global ThoiGian
    	#global GhiChu

    	#x=datetime.datetime.now()
    	#date=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
    	self.MyThreadFirebase=dulieuFirebase()
    	self.MyThreadFirebase.start()
    	self.MyThreadFirebase.sig2.connect(self.on_info_firebase)
    	self.MyThreadFirebase.sig3.connect(self.on_info_firebase)
    	self.MyThreadFirebase.sig4.connect(self.on_info_firebase)
    	self.MyThreadFirebase.sig5.connect(self.on_info_firebase)
    	self.MyThreadFirebase.sig6.connect(self.on_info_firebase)
    	

    def on_info_datetime(self,gio):
        self.dateTimeEdit.setDateTime(gio)
        
    def Load_Data_Hours(self):
    	global gio
    	gio=QDateTime.currentDateTime()
    	print("nowdate:",gio)
    	self.MyThread=Thread()
    	self.MyThread.start()
    	self.MyThread.sig1.connect(self.on_info_datetime)

    def retranslateUi(self, MainWindow):
    	_translate = QtCore.QCoreApplication.translate
    	MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    	self.lblTieuDe.setText(_translate("MainWindow", "ỨNG DỤNG TỦ THUỐC GIA ĐÌNH"))
    	self.btnGiupdo.setText(_translate("MainWindow", "Giúp đỡ"))
    	self.lblDonThuoc.setText(_translate("MainWindow", "Đơn thuốc"))
    	self.lblTenthuoc.setText(_translate("MainWindow", "Tên thuốc"))
    	self.lblLieuluong.setText(_translate("MainWindow", "Liều lượng"))
    	self.lblThoigian.setText(_translate("MainWindow", "Thời gian"))
    	self.lblGhiChu.setText(_translate("MainWindow", "Ghi chú"))
    	self.btnDaXem.setText(_translate("MainWindow", "Đã xem"))
    	self.btnThietlaplai.setText(_translate("MainWindow", "Thiết lập lại"))


class Thread(QThread):
	sig1=pyqtSignal(QDateTime)

	def __init__(self):
		super(Thread,self).__init__()

	def run(self):
		self.running=True
		global gio
		while self.running:
			gio=QDateTime.currentDateTime()
			self.sig1.emit(gio)
			print("updategio:",gio)
			time.sleep(1)

class dulieuFirebase(QThread):
	sig2=pyqtSignal(datetime.datetime)
	sig3=pyqtSignal(str)
	sig4=pyqtSignal(str)
	sig5=pyqtSignal(str)
	sig6=pyqtSignal(str)
	sig7=pyqtSignal(int)

	def __init__(self):
		super(dulieuFirebase, self).__init__()

	def run(self):
		global x
		global TenThuoc
		global LieuLuong
		global ThoiGian
		global GhiChu
		global firebase
		global Row
		global dx
		dx=0
		gio=['','','','','','','','','','']
		try:
			firebase = firebase.FirebaseApplication('https://dulieu-eeecc.firebaseio.com',None)
		except:
			pass
		else:
			pass
		
		while True:
			x=datetime.datetime.now()
			date=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
			currenttime=str(x.hour)+':'+str(x.minute)
			print("thoi gian hien tai",currenttime)
			Row=-1
			for s in range (1,10):
				try:
					result = firebase.get('',str(s)+'/'+date)
					if result==None: break
					TenThuoc=result["tenthuoc"]
					LieuLuong=result["lieuluong"]
					ThoiGian=result["thoigian"]
					GhiChu=result["ghichu"]
					self.sig2.emit(x)
					self.sig3.emit(TenThuoc)
					self.sig4.emit(LieuLuong)
					self.sig5.emit(ThoiGian)
					self.sig6.emit(GhiChu)
					Row=Row+1
					gio[s-1]=ThoiGian
					print("dang lay du lieu")
				except:
					print("mat ket noi2")	
				else:
					print("khong co loi2")
			for i in range(0,10):
				if currenttime==gio[i]:
					flat=1
					break
				else:
					flat=0
			if flat==1 and dx==0:
				print("dx=",dx)
				while flat==1:
					print("da den luc",gio[i])
					pygame.init()
					pygame.mixer.music.load('/home/pi/Desktop/New/speakdata.mp3')
					pygame.mixer.music.play()
					time.sleep(10)
					for i in range(0,10):
						if currenttime!=gio[i]:
							flat=0
							break	
			else:
				print("chua den luc")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())

