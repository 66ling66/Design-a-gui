from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QStackedLayout,QLabel,QApplication
import sys
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Create_stack_layout()
        self.init_ui()

    def init_ui(self):

        container=QVBoxLayout()         #1.创建一个大的垂直布局器
        self.setWindowTitle('抽屉布局器')
        self.resize(1000,750)

        widget=QWidget()                #2.创建一个可显示的窗口用来显示窗口
        widget.setLayout(self.stack)    #3.这个窗口的布局设置为抽屉布局
        widget.setStyleSheet('background-color:white;')

        btn1=QPushButton('按钮1')
        btn2=QPushButton('按钮2')


        btn1.clicked.connect(self.click_btn1)       #4.将按钮生效连接到一个作用中

        btn2.clicked.connect(self.click_btn2)

        container.addWidget(widget)     #5.往最大的布局器里分别加上抽屉，按钮
        container.addWidget(btn1)
        container.addWidget(btn2)
        self.setLayout(container)       #应用该布局

    def Create_stack_layout(self):

        self.stack=QStackedLayout()     #创建一个抽屉布局

        win1=window1()  #设置抽屉

        win2=window2()
        self.stack.addWidget(win1)  #往这个布局里加入抽屉
        self.stack.addWidget(win2)

    def click_btn1(self):
        self.stack.setCurrentIndex(0)       #点击按钮后执行的操作
    def click_btn2(self):
        self.stack.setCurrentIndex(1)

class window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉1',self)
        self.setStyleSheet('background-color:green;')


class window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉2',self)
        self.setStyleSheet('background-color:green;')


if __name__=='__main__':
    app=QApplication(sys.argv)

    w=Mywindow()

    w.show()

    app.exec_()
