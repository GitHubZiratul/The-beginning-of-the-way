import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.QtWidgets import QGridLayout , QLabel, QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,QSize
from PyQt5 import QtGui
import pygame

class Multi(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def form_1(self):
		self.firstWindow = QWidget(self)
		self.fon = QPushButton('', self.firstWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		

		self.setWindowTitle('Window 1')

		Quit = QPushButton('', self.firstWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))



		self.text1 = QPushButton('', self.firstWindow)
		self.text1.move(100,200) 
		self.text1.setGeometry(80,100,600,110)
		self.text1.setIcon(QIcon('text1.png'))
		self.text1.setFlat(True)
		self.text1.setIconSize(QSize(450,700))


		self.text1_1 = QPushButton('', self.firstWindow)
		self.text1_1.move(100,200) 
		self.text1_1.setGeometry(80,180,600,110)
		self.text1_1.setIcon(QIcon('text1_1.png'))
		self.text1_1.setFlat(True)
		self.text1_1.setIconSize(QSize(450,700))


		self.text1_2 = QPushButton('', self.firstWindow)
		self.text1_2.move(100,200) 
		self.text1_2.setGeometry(80,250,600,110)
		self.text1_2.setIcon(QIcon('text1_2.png'))
		self.text1_2.setFlat(True)
		self.text1_2.setIconSize(QSize(450,700))


		self.osmkar = QPushButton('', self.firstWindow)
		self.osmkar.clicked.connect(self.next)
		self.osmkar.move(100,200) 
		self.osmkar.setGeometry(45,600,300,70)
		self.osmkar.setIcon(QIcon('osmkar.png'))
		self.osmkar.setIconSize(QSize(250,60))
		self.osmkar.setFlat(True)

		


		self.osmkom = QPushButton('', self.firstWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(400,600,300,70)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(250,60))
		self.osmkom.setFlat(True)

		self.povolosps = QPushButton('', self.firstWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(250,700,300,70)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(250,60))
		self.povolosps.setFlat(True)

	



	def form_2(self):
		self.secondWindow = QWidget(self)

		self.fon = QPushButton('', self.secondWindow)
		self.fon.setIcon(QIcon('telefon.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.text1 = QPushButton('', self.secondWindow)
		self.text1.move(100,200) 
		self.text1.setGeometry(80,100,600,110)
		self.text1.setIcon(QIcon('telefon.png'))
		self.text1.setFlat(True)
		self.text1.setIconSize(QSize(450,700))


		self.text1_1 = QPushButton('', self.secondWindow)
		self.text1_1.move(100,200) 
		self.text1_1.setGeometry(80,180,600,110)
		self.text1_1.setIcon(QIcon('telefon2.png'))
		self.text1_1.setFlat(True)
		self.text1_1.setIconSize(QSize(450,700))

		self.osmkar = QPushButton('', self.secondWindow)		
		self.osmkar.move(100,200) 
		self.osmkar.setGeometry(45,600,300,70)
		self.osmkar.setIcon(QIcon('tel_deistv1.png'))
		self.osmkar.setIconSize(QSize(250,60))
		self.osmkar.setFlat(True)
		self.osmkar.clicked.connect(self.next1)
		self.osmkar.clicked.connect(self.ring)
		


		self.osmkom = QPushButton('', self.secondWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(400,600,300,70)
		self.osmkom.setIcon(QIcon('tel_deistv2.png'))
		self.osmkom.setIconSize(QSize(250,60))
		self.osmkom.setFlat(True)

		



		Quit = QPushButton('', self.secondWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))



	def form_3(self):
		self.thirdWindow = QWidget(self)
		
		
		self.fon = QPushButton('', self.thirdWindow)
		self.fon.setIcon(QIcon('telefon.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.zvonok = QPushButton('', self.thirdWindow)
		self.zvonok.move(100,200) 
		self.zvonok.setGeometry(80,180,600,110)
		self.zvonok.setIcon(QIcon('zvonok.png'))
		self.zvonok.setFlat(True)
		self.zvonok.setIconSize(QSize(450,700))

		self.police = QPushButton('', self.thirdWindow)		
		self.police.move(100,200) 
		self.police.setGeometry(45,600,300,70)
		self.police.setIcon(QIcon('police.png'))
		self.police.setIconSize(QSize(250,60))
		self.police.setFlat(True)
		self.police.clicked.connect(self.next3)


		self.roditeli = QPushButton('', self.thirdWindow)		
		self.roditeli.move(100,200) 
		self.roditeli.setGeometry(400,600,300,70)
		self.roditeli.setIcon(QIcon('roditeli.png'))
		self.roditeli.setIconSize(QSize(250,60))
		self.roditeli.setFlat(True)
		self.roditeli.clicked.connect(self.next2)
		self.roditeli.clicked.connect(self.gudok)

		Quit = QPushButton('', self.thirdWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_4(self):
		self.fourthWindow= QWidget(self)
		
		
		self.fon = QPushButton('', self.fourthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.niktonepodoshol = QPushButton('', self.fourthWindow)
		self.niktonepodoshol.move(100,200) 
		self.niktonepodoshol.setGeometry(80,180,600,110)
		self.niktonepodoshol.setIcon(QIcon('niktonepodoshol.png'))
		self.niktonepodoshol.setFlat(True)
		self.niktonepodoshol.setIconSize(QSize(450,700))

		self.telefonoff = QPushButton('', self.fourthWindow)
		self.telefonoff.move(100,200) 
		self.telefonoff.setGeometry(80,250,600,110)
		self.telefonoff.setIcon(QIcon('telefonoff.png'))
		self.telefonoff.setFlat(True)
		self.telefonoff.setIconSize(QSize(450,700))

		

		self.osmkom = QPushButton('', self.fourthWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(180,600,400,90)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(400,100))
		self.osmkom.setFlat(True)


		self.povolosps = QPushButton('', self.fourthWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(200,700,400,90)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(400,100))
		self.povolosps.setFlat(True)

		Quit = QPushButton('', self.fourthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))


	def form_5(self):
		self.fifthWindow= QWidget(self)


		
		self.fon = QPushButton('', self.fifthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))	

		self.objas = QPushButton('', self.fifthWindow)
		self.objas.move(100,200) 
		self.objas.setGeometry(80,180,600,110)
		self.objas.setIcon(QIcon('objas.png'))
		self.objas.setFlat(True)
		self.objas.setIconSize(QSize(600,700))



		self.telefonoff = QPushButton('', self.fifthWindow)
		self.telefonoff.move(100,200) 
		self.telefonoff.setGeometry(80,250,600,110)
		self.telefonoff.setIcon(QIcon('telefonoff.png'))
		self.telefonoff.setFlat(True)
		self.telefonoff.setIconSize(QSize(450,700))


		self.osmkom = QPushButton('', self.fifthWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(180,600,400,90)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(400,100))
		self.osmkom.setFlat(True)
	


		self.povolosps = QPushButton('', self.fifthWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(200,700,400,90)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(400,100))
		self.povolosps.setFlat(True)

		Quit = QPushButton('', self.fifthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_6(self):
		self.sixthWindow= QWidget(self)

		self.fon = QPushButton('', self.komnatajpeg)
		self.fon.setIcon(QIcon('komnatajpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))	

		



		Quit = QPushButton('', self.fifthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		

	def initUI(self):
		self.setGeometry(400,0,700,1000)
		self.form_1()
		self.setCentralWidget(self.firstWindow)






		self.setWindowTitle('QUEST')
		self.setWindowIcon(QIcon('mxeb2NK.png'))

		

		self.show()

	def next(self):
		self.form_2()
		self.setCentralWidget(self.secondWindow)

	

	def next1(self):
		self.form_3()
		self.setCentralWidget(self.thirdWindow)

	def next2(self):
		self.form_4()
		self.setCentralWidget(self.fourthWindow)

	def next3(self):
		self.form_5()
		self.setCentralWidget(self.fifthWindow)

	def next4(self):
		self.form_6()
		self.setCentralWidget(self.sixthWindow)


	def dver(self):
		pygame.init()
		pygame.mixer.music.load('skrip-dveri-dver-zahlopyvaetsya.mp3')
		pygame.mixer.music.play()	

	def ring(self):
		pygame.init()
		pygame.mixer.music.load('Zvuk-nabor_nomera_telef.mp3')
		pygame.mixer.music.play()	

	def gudok(self):
		pygame.init()
		pygame.mixer.music.load('04337.mp3')
		pygame.mixer.music.play()	


	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Подтверждение',
			"Вы действительно хотите выйти ?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		


app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())
ex = Multi()



