import json
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QThread,pyqtSignal
import sys
import requests

class Loginthread(QThread):        #创建一个子线程类
    star_login_signal=pyqtSignal(str)
    def __init__(self,signal):
        super().__init__()
        self.login_state_signal=signal
    def login_by_request(self,user_password_json):      #收到信号后执行此函数
        user_password_json=json.loads(user_password_json)       #将json格式转为dict格式
        '''向腾讯服务器发送请求 同时将要传输的数据加上，传入形式为dict'''
        r=requests.post(url='https://service-irxc4z8s-1320189272.gz.apigw.tencentcs.com/release/Login',json=user_password_json)
        print(json.loads(r.content))
        print(json.loads(r.content)['login_state'])
        self.login_state_signal.emit(json.loads(r.content)['login_state'])      #给主进程发送信号
    def run(self):
        while True:
            print('子线程正在运行')
            time.sleep(1)





class Mywindow(QWidget):
    my_signal = pyqtSignal(str)     #创建一个自定义信号
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.ui=uic.loadUi('login.ui')
        # print(self.ui.__dict__)
        self.user_name=self.ui.lineEdit#用户账号
        self.pass_word=self.ui.lineEdit_2   #用户密码

        self.btn1=self.ui.pushButton   #
        self.btn2=self.ui.pushButton_2  #获取登录和忘记密码的信息
        self.textbrowser=self.ui.textBrowser    #文本展示器
        self.textbrowser.setReadOnly(False)   #表示文本可更改


        self.my_signal.connect(self.login_state)
        self.btn1.clicked.connect(self.login)
        self.loginthread=Loginthread(self.my_signal)      # 添加一个子线程，让费时间的事情放在子线程里面跑 同时把一个信号传进去，这样就可以把子进程里的信号传回到主进程
        self.loginthread.star_login_signal.connect(self.loginthread.login_by_request)     #将信号与槽绑定 即信号发送后该做什么
        self.loginthread.start()    #让子线程跑起来    # 注意一定要加上self让其变为成员变量，否则当一个函数执行完后python会将该变量清除导致报错


    def login(self):

        '''定义用户登录的效果'''
        user_name = self.user_name.text()
        pass_word = self.pass_word.text()
        '''发送信号，执行子进程中特定的函数 dumps是将python字典格式转换为json字符串格式，因为信号传输刚开始设定的是str'''
        self.loginthread.star_login_signal.emit(json.dumps({'user_name':user_name,'pass_word':pass_word}))
    def login_state(self,state):
        self.textbrowser.setText(state)



if __name__=='__main__':
    app=QApplication(sys.argv)

    w=Mywindow()

    w.ui.show()
    app.exec_()