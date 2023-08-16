from PyQt5.QtWidgets import *
import sys

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle('网状分布')
        self.resize(1000,750)

        data={0:[7,8,9,'+','('],
              1:[4,5,6,'-',')'],
              2:[1,2,3,'*','<-'],
              3:[0,'.','=','/','C']}

        container=QVBoxLayout()
        edit=QLineEdit()
        edit.setPlaceholderText('请输入内容')
        container.addStretch(1)
        container.addWidget(edit)
        container.addStretch(0)
        grid=QGridLayout()
        for line_number,line_data in data.items():
            for i,content in enumerate(line_data):
                content=str(content)
                btn=QPushButton(content)
                grid.addWidget(btn,line_number,i)

        container.addLayout(grid)
        container.addStretch(1)
        self.setLayout(container)

if __name__=='__main__':
    app=QApplication(sys.argv)

    w=Mywindow()
    w.show()

    app.exec_()