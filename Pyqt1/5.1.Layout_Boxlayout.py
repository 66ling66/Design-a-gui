from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QMainWindow
import sys

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 700)

        self.setWindowTitle('垂直布局')
        #
        btn1=QPushButton('BUtton1')
        #
        btn2=QPushButton('Button2')
        #
        btn3=QPushButton('Button3')

        # layout.addStretch()
        layout = QVBoxLayout()   #创建一个垂直布局器
        layout.addStretch()      #添加控制比例的控件 无参数则按平均的方式
        layout.addWidget(btn1)   #往布局器里加入按钮
        layout.addStretch()
        layout.addWidget(btn2)
        layout.addStretch()
        layout.addWidget(btn3)
        layout.addStretch()
        self.setLayout(layout)  #启用布局器


if __name__=='__main__':
    app=QApplication(sys.argv)

    w=Mywindow()

    w.show()

    app.exec_()
