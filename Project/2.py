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

		
		

		
		

		self.autorisation = QPushButton('', self)
		self.autorisation.move(100,200) 
		self.autorisation.setGeometry(210,200,300,65)
		self.autorisation.setIcon(QIcon('autorisation.png'))
		self.autorisation.setFlat(True)
		self.autorisation.setIconSize(QSize(500,700))


		self.registation = QPushButton('', self)
		self.registation.move(100,200) 
		self.registation.setGeometry(210,300,300,65)
		self.registation.setIcon(QIcon('registation.png'))
		self.registation.setFlat(True)
		self.registation.setIconSize(QSize(450,700))


		
		
		Quit = QPushButton('', self)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())

		Quit.move(0,0) 
		Quit.setGeometry(600,0,100,100)
		Quit.setIcon(QIcon('power.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(100,100))
		
		
		self.show() 

	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Подтверждение',
			"Are you sure to quit ?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		

		


