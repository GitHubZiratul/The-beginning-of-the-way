import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout , QLabel, QLineEdit
from PyQt5.QtWidgets import QMainWindow

class Multi(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def form_1(self):
		self.firstWindow = QWidget(self)
		self.but1 = QPushButton('next', self.firstWindow)
		self.but1.clicked.connect(self.next)
		self.setWindowTitle('Window 1')

	def form_2(self):
		self.secondWindow = QWidget(self)
		self.but2 = QPushButton('back', self.secondWindow)
		self.but2.clicked.connect(self.back)
		self.setWindowTitle('Window 2')

	def initUI(self):
		self.setGeometry(100, 100, 450, 250)
		self.form_1()
		self.setCentralWidget(self.firstWindow)
		self.show()

	def next(self):
		self.form_2()
		self.setCentralWidget(self.secondWindow)

	def back(self):
		self.form_1()
		self.setCentralWidget(self.firstWindow)

app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())




