from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QMainWindow
from PyQt5.QtGui import QIcon


import sys

class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.initUI()

	


	def initUI(self):
		self.window1 = QWidget() 
		grid = QGridLayout()
		grid.setSpacing(20)
		self.button1 = QPushButton('Нажми1')
		self.button2 = QPushButton('Нажми2')
		self.button3 = QPushButton('Нажми3')
		grid.addWidget(self.button1, 0, 0)
		grid.addWidget(self.button2, 1, 0)
		grid.addWidget(self.button3, 2, 0)
		self.button1.clicked.connect(self.next)

		self.window1.setLayout(grid)
		
		self.window2 = QWidget()
		grid = QGridLayout()
		grid.setSpacing(20)
		self.firstText = QLabel()
		self.button4 = QPushButton('не работает')
		grid.addWidget(self.firstText, 0, 0)
		grid.addWidget(self.button4, 0, 1)
		self.window2.setLayout(grid)

		self.setCentralWidget(self.window1)

		self.setGeometry(100, 100, 700, 500)
		self.show()
		
	def next(self):
		self.setCentralWidget(self.window2)




app = QApplication(sys.argv)
my_window = Change()
sys.exit(app.exec_())