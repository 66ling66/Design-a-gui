from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QMainWindow,QGroupBox,QRadioButton,QHBoxLayout
import sys

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.resize(1000,750)
        container=QVBoxLayout()  #创建一个容器，可以指定布局

        group1=QGroupBox('姓名')  #创建一个组
        layout1=QVBoxLayout()    #创建一个布局
        btn1=QRadioButton('小明')
        btn2=QRadioButton('小红')
        layout1.addWidget(btn1)
        layout1.addWidget(btn2)

        '''layout2=QHBoxLayout()
        btn1=QRadioButton('小心')
        btn2=QRadioButton('小花')
        layout2.addWidget(btn1)
        layout2.addWidget(btn2)'''
        group1.setLayout(layout1)#将布局加到组里
        # group1.setLayout(layout2) 一个组里好像只能有一个布局 组貌似是最小单位了

        group2=QGroupBox('年龄')
        layout2=QHBoxLayout()
        btn1=QRadioButton('18')
        btn2=QRadioButton('19')
        btn3=QRadioButton('20')
        layout2.addWidget(btn1)
        layout2.addWidget(btn2)
        layout2.addWidget(btn3)
        group2.setLayout(layout2)


        container.addWidget(group1)
        container.addWidget(group2)
        self.setLayout(container)



if __name__=='__main__':
    app=QApplication(sys.argv)

    w=Mywindow()

    w.show()

    app.exec_()
