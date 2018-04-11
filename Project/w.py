import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,QSize
from PyQt5 import QtGui
# self.name.setFlat(True) 


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.setWindowTitle('QUEST')
		self.setWindowIcon(QIcon('mxeb2NK.png'))

		self.setGeometry(500, 50, 700, 1000)

		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('fon.png'))
		self.fon.setGeometry(0,0,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		
		

		self.nameText = QLabel('''Ты очухиваещься в темном помещении
ничего не видно , ты хочешь выбраться отсюда''', self)
		self.nameText.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
		

		self.Pocket = QPushButton('Осмотреть карманы', self)
		self.Pocket.move(100,200) 
		self.Pocket.setGeometry(300,400,150,30)

		
		
		Quit = QPushButton('Выход', self)
		Quit.move(300,500) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())

		
		
		self.show() 

	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Подтверждение',
			"Are you sure to quit ?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		

		


app = QApplication(sys.argv)
my_window = Example()
sys.exit(app.exec_())
ex = Example()