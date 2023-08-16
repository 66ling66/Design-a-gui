import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QDialog,QLabel

class mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):      #初始化你的ui界面
        self.resize(1000,750)
        container=QVBoxLayout()

        btn1=QPushButton('按钮1')

        container.addWidget(btn1)
        self.setLayout(container)
        btn1.clicked.connect(self.click_btn)            #绑定信号
    def click_btn(self):
        dia=dialog()
        dia.show()
class dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        # self.setWindowTitle('警告')
        self.resize(100,75)
        QLabel('已经收到点击信号',self)
        self.exec()

if __name__=='__main__':
    app=QApplication(sys.argv)

    w=mywindow()
    w.show()

    app.exec_()

