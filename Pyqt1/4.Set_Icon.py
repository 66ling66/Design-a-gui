from PyQt5.QtWidgets import QApplication,QWidget
import sys
from PyQt5.QtGui import QIcon

if __name__=='__main__':
    app=QApplication(sys.argv)      #创建一个app对象

    w=QWidget()     #小组件，即窗口

    w.setWindowTitle('the first app')
    w.setWindowIcon(QIcon('image.jpg'))     #设置图标
    w.show()

    app.exec_()  #让这个app一直循环地跑