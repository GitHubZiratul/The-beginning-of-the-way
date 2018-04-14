import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout , QLabel, QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,QSize
from PyQt5 import QtGui


class Multi(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.setGeometry(500, 50, 700, 1000)
		self.form_1()
		self.setCentralWidget(self.firstWindow)

		Quit = QPushButton('', self)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())

		Quit.move(0,0) 
		Quit.setGeometry(640,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
		self.show()

	def form_1(self):
		self.firstWindow = QWidget(self)
		self.fon = QPushButton('', self.firstWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.text1 = QPushButton('', self)
		self.text1.move(100,200) 
		self.text1.setGeometry(80,100,600,110)
		self.text1.setIcon(QIcon('text1.png'))
		self.text1.setFlat(True)
		self.text1.setIconSize(QSize(450,700))


		self.text1_1 = QPushButton('', self)
		self.text1_1.move(100,200) 
		self.text1_1.setGeometry(80,180,600,110)
		self.text1_1.setIcon(QIcon('text1_1.png'))
		self.text1_1.setFlat(True)
		self.text1_1.setIconSize(QSize(450,700))


		self.text1_2 = QPushButton('', self)
		self.text1_2.move(100,200) 
		self.text1_2.setGeometry(80,250,600,110)
		self.text1_2.setIcon(QIcon('text1_2.png'))
		self.text1_2.setFlat(True)
		self.text1_2.setIconSize(QSize(450,700))




		

		self.osmkar = QPushButton('next', self.firstWindow)
		self.osmkar.clicked.connect(self.next)
		self.osmkar.move(100,200) 
		self.osmkar.setGeometry(45,600,300,70)
		self.osmkar.setIcon(QIcon('osmkar.png'))
		self.osmkar.setIconSize(QSize(250,60))
		self.osmkar.setFlat(True)

		self.setWindowTitle('QUEST')
		self.setWindowIcon(QIcon('mxeb2NK.png'))


		self.osmkom = QPushButton('', self.firstWindow)
		self.osmkar.clicked.connect(self.next2)
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(400,600,300,70)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(250,60))
		self.osmkom.setFlat(True)

		self.povolosps = QPushButton('', self)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(250,700,300,70)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(250,60))
		self.povolosps.setFlat(True)

		
		
		
		
		
		self.show() 
		
	


	def form_2(self):
		self.secondWindow = QWidget(self)

		self.fon1 = QPushButton('', self.secondWindow)
		self.fon1.setIcon(QIcon('fon3.jpeg'))

		
		self.fon1.setGeometry(0,-100,700,1000)
		self.fon1.setIcon(QIcon('fon'))


		
	def form_3(self):
		self.thirdWindow = QWidget(self)
	def form_4(self):
		self.fifthWindow = QWidget(self)
		







	def next(self):
		self.form_2()
		self.setCentralWidget(self.secondWindow)
	def next2(self):
		self.form_3()
		self.setCentralWidget(self.thirdWindow)
	def next3(self):
		self.form_4()
		self.setCentralWidget(self.fifthWindow)



	




app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())
my_window = Example()
ex = Example()



