# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 632)
        MainWindow.setIconSize(QtCore.QSize(35, 35))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 80, 301, 421))
        self.frame.setStyleSheet("#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 50, 141, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial Rounded MT Bold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 151, 31))
        self.label_2.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 110, 271, 371))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-left-right-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(222, 0, 51, 31))
        self.pushButton.setStyleSheet("QpushButton{\n"
"    border:none;\n"
"}\n"
"QpushButton:hover{\n"
"    padding-bottom:5px;\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/按钮.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 30, 271, 341))
        self.frame_3.setMinimumSize(QtCore.QSize(271, 341))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("\n"
"QpushButton：pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_7)
        self.stackedWidget_2.setStyleSheet("#pushButton_confirm{\n"
"    border:none;\n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"}\n"
"#pushButton_confirm_2:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"#pushButton_confirm:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.login)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_account = QtWidgets.QLineEdit(self.login)
        self.lineEdit_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.verticalLayout_5.addWidget(self.lineEdit_account)
        self.lineEdit_password = QtWidgets.QLineEdit(self.login)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_5.addWidget(self.lineEdit_password)
        self.pushButton_confirm = QtWidgets.QPushButton(self.login)
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.verticalLayout_5.addWidget(self.pushButton_confirm)
        self.stackedWidget_2.addWidget(self.login)
        self.register_2 = QtWidgets.QWidget()
        self.register_2.setStyleSheet("#pushButton_confirm_2{\n"
"    border:none;\n"
"}\n"
"#pushButton_confirm_2:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.register_2.setObjectName("register_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.register_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_R_account = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_R_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_account.setObjectName("lineEdit_R_account")
        self.verticalLayout_6.addWidget(self.lineEdit_R_account)
        self.lineEdit_R_password1 = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_R_password1.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password1.setObjectName("lineEdit_R_password1")
        self.verticalLayout_6.addWidget(self.lineEdit_R_password1)
        self.lineEdit_R_password2 = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_R_password2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password2.setObjectName("lineEdit_R_password2")
        self.verticalLayout_6.addWidget(self.lineEdit_R_password2)
        self.pushButton_confirm_2 = QtWidgets.QPushButton(self.register_2)
        self.pushButton_confirm_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_confirm_2.setStyleSheet("color: rgb(85, 170, 255);")
        self.pushButton_confirm_2.setObjectName("pushButton_confirm_2")
        self.verticalLayout_6.addWidget(self.pushButton_confirm_2)
        self.stackedWidget_2.addWidget(self.register_2)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("\n"
"#pushButton_login:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px\n"
"}\n"
"\n"
"#pushButton_register:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_login.setStyleSheet("")
        self.pushButton_login.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/登录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_login.setIcon(icon1)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_register.setStyleSheet("")
        self.pushButton_register.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/注册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_register.setIcon(icon2)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.pushButton_register.raise_()
        self.pushButton_login.raise_()
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"幼圆\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"幼圆\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        self.label_7.setStyleSheet("\n"
"font: 12pt \"幼圆\";\n"
"color: rgb(85, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"幼圆\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.page_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"幼圆\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to my app"))
        self.label_2.setText(_translate("MainWindow", "Nice to see you\n"
" I love you"))
        self.lineEdit_account.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "密码："))
        self.pushButton_confirm.setText(_translate("MainWindow", "确认"))
        self.lineEdit_R_account.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_R_password1.setPlaceholderText(_translate("MainWindow", "密码："))
        self.lineEdit_R_password2.setPlaceholderText(_translate("MainWindow", "确认密码："))
        self.pushButton_confirm_2.setText(_translate("MainWindow", "确认"))
        self.label_5.setText(_translate("MainWindow", "输入账号密码为空"))
        self.label_6.setText(_translate("MainWindow", "两次输入密码不一致"))
        self.label_7.setText(_translate("MainWindow", "注册成功，欢迎使用"))
        self.label_3.setText(_translate("MainWindow", "账号或密码不能为空"))
        self.label_4.setText(_translate("MainWindow", "密码错误"))
import res_rc
