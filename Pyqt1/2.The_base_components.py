from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit
import sys

if __name__=='__main__':
    app=QApplication(sys.argv)      #创建一个app对象

    w=QWidget()     #小组件，即窗口

    w.setWindowTitle('the first app')

    # 创建一个label（纯文本）
    label = QLabel('账号：', w)  # 在生成组件地时候就已经设置好了父类对象
    label.setGeometry(20, 20, 30, 20)

    #创建一个文本框即输入文本的组件
    edit=QLineEdit(w)
    edit.setPlaceholderText('请输入账号:')
    edit.setGeometry(55,20,100,20)



    #创建一个按钮
    btn1=QPushButton('button')      #设置按钮
    btn1.setGeometry(75,45,50,20)       #设置x,y,h,w
    btn1.setParent(w)  # 设置父亲对象








    w.show()

    app.exec_()  #让这个app一直循环地跑