from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
import webbrowser
import sys
from LoginUI import *
from interfaceUI import *
import psycopg2
#pyrcc5 -o res_rc.py res.qrc  这行代码将.qrc文件转化为.py文件
#python -m PyQt5.uic.pyuic LoginUI.ui -o LoginUI.py 这行代码将.ui文件转化为.py文件  在终端运行


user_now=''
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow1()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)       #将多余的两行去掉

        #设置点击登录界面和注册界面的效果
        self.ui.pushButton_login.clicked.connect(lambda : self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_register.clicked.connect(lambda : self.ui.stackedWidget_2.setCurrentIndex(1))
        #设计关闭效果
        self.ui.pushButton.clicked.connect(lambda : self.close())
        #登录跳转界面
        self.ui.pushButton_confirm.clicked.connect(self.Login_in)
        #注册界面
        self.ui.pushButton_confirm_2.clicked.connect(self.register)
    def Login_in(self):
        account=self.ui.lineEdit_account.text()
        password=self.ui.lineEdit_password.text()
        conn=psycopg2.connect(database='dataMy',user='postgres',password='2207469397peng',host='127.0.0.1',port='5432')
        cur=conn.cursor()
        cur.execute('select * from users')
        rows=cur.fetchall()
        data={}
        for row in rows:
            data[row[0]]=row[1]
        conn.commit()
        conn.close()
        if len(account)==0 or len(password)==0:
            self.ui.stackedWidget.setCurrentIndex(4)
        else:
            if account in data and data[account]==password:
                global user_now
                user_now=account
                self.win=Mainwindow()
                self.close()
                self.win.show()
            else:
                print(0)
                self.ui.stackedWidget.setCurrentIndex(5)
    def register(self):
        account=self.ui.lineEdit_R_account.text()
        password1=self.ui.lineEdit_R_password1.text()
        password2=self.ui.lineEdit_R_password2.text()

        if len(password2) + len(password1) + len(account)==0:
            print(4)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif password1!=password2:
            self.ui.stackedWidget.setCurrentIndex(2)
        else:
            conn = psycopg2.connect(database='dataMy', user='postgres', password='2207469397peng', host='127.0.0.1',
                                    port='5432')
            cur = conn.cursor()
            cur.execute(f"insert into users values('{account}','{password1}')")
            conn.commit()
            conn.close()
            self.ui.stackedWidget.setCurrentIndex(3)





class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)       #将多余的两行去掉

        #设置点击登录界面和注册界面的效果
        self.ui.pushButton_home.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_web.clicked.connect(self.go_web)
        self.ui.pushButton_my.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_logout.clicked.connect(self.log_out)
        #设计关闭效果
        self.ui.pushButton_close.clicked.connect(lambda : self.close())
        #修改密码
        self.ui.pushButton_confirm_password.clicked.connect(self.changepassword)
    def changepassword(self):
        password1=self.ui.lineEdit_password1.text()
        password2=self.ui.lineEdit_password2.text()
        temp=len(password1)+len(password2)

        if temp==0:
            self.ui.label_3.setText('密码不能为空')
        elif password1!=password2:
            self.ui.label_3.setText('两次输入密码不一致')
        else:
            conn = psycopg2.connect(database='dataMy', user='postgres', password='2207469397peng', host='127.0.0.1',
                                    port='5432')
            cur = conn.cursor()
            global user_now
            '''更新数据库里的密码'''
            cur.execute(f"update users set passwords='{password2}' where accounts='{user_now}'")
            conn.commit()
            conn.close()
            self.ui.label_3.setText('密码修改成功')


    def go_web(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton_github.clicked.connect(lambda : webbrowser.open('https://github.com'))
        self.ui.pushButton_claude.clicked.connect(lambda : webbrowser.open('https://www.anthropic.com/index/claude-2'))

    def log_out(self):
        global user_now
        self.close()
        self.login=LoginWindow()
        self.login.show()



















if __name__=='__main__':
    w = QApplication(sys.argv)
    app=LoginWindow()
    app.show()

    w.exec_()




