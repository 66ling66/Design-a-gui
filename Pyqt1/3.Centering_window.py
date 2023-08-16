from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget
import sys




if __name__=='__main__':
    app=QApplication(sys.argv)      #创建一个app对象

    w=QWidget()     #小组件，即窗口

    w.setWindowTitle('the first app')

    centerpoint=QDesktopWidget().availableGeometry().center()  #获取屏幕的中心坐标数据
    x,y=centerpoint.x(),centerpoint.y()             #分别获取x,y坐标

    w_x,w_y,height,width=w.frameGeometry().getRect()        #获取窗口的x,y,height,width

    w.move(x-(height//2),y-(width//2))      #将窗口移动到中心


    w.show()

    app.exec_()  #让这个app一直循环地跑