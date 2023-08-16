from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout
from PyQt5.QtCore import pyqtSignal
import sys
class mywindow(QWidget):
    my_signal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.resize(1000,750)
        container=QVBoxLayout()     #创建一个容器

        btn=QPushButton('按钮1')


        container.addWidget(btn)
        btn.clicked.connect(self.check)         #连接信号与槽
        self.setLayout(container)

        self.my_signal.connect(self.slot)   #连接信号与槽

    def check(self):        #定义一个槽
        for i,id in enumerate(['192.168.1.%d' % x for x in range(10)]):
            print('第%d次检查，检查ip为:%s' % (i,id))
            if i == 5:
                self.my_signal.emit(str(i))         #执行my

    def slot(self,msg):     #定义一个槽
        print(msg)

if __name__=='__main__':
    app=QApplication(sys.argv)

    w=mywindow()

    w.show()

    app.exec_()


