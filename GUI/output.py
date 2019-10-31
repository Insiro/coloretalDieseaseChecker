import sys
from PyQt5 import QtWidgets, QtGui
import test as predict
#import test


class MyApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.imagelabel = QtWidgets.QLabel()
        inputBtn = QtWidgets.QPushButton('input Image')
        self.resultlabel1 = QtWidgets.QLabel()
        self.resultlabel2 = QtWidgets.QLabel()
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        semi = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        # file Input
        openFile = QtWidgets.QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('input the image')
        openFile.triggered.connect(self.showDialog)

        # bitmap

        self.resultlabel1.setText('result : ')
        self.resultlabel2.setText('        ')
        self.imagelabel.setPixmap(QtGui.QPixmap().scaled(100, 100))
        # inputBtn.addAction()
        inputBtn.clicked.connect(self.showDialog)
        inputBtn.setToolTip('input the image')
        self.textEdit = QtWidgets.QTextEdit()

        # 자측 빈공간
        semi.addWidget(self.resultlabel1)
        semi.addWidget(self.resultlabel2)
        vbox.addStretch(1)
        vbox.addLayout(semi)
        vbox.addStretch(1)
        vbox.addWidget(inputBtn)
        vbox.addStretch(1)
        hbox.addWidget(self.imagelabel)
        hbox.addLayout(vbox)
        self.setWindowTitle('VGG model prediction')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            # self.resultlabel2.setText(fname[0])
            # self.resultlabel2.update()
            tempimg = QtGui.QPixmap(fname[0]).scaled(100, 100)
            self.imagelabel.setPixmap(tempimg)
            self.imagelabel.update()
            result = '{0:2.2f}% normal'.format(predict.get_result(fname[0]))
            self.resultlabel2.setText(result)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
