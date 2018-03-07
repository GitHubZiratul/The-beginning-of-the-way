from time import sleep #Из модуля time импортируем атрибут sleep 

class Typical_dag_05: #Создание класса 
	favorite_phrase = 'Жи есть' #Описание класса 
	red_moccasins = True #
	iq = 80 #Скорее 60-70 
	respect_to_elders = None # 

	def no_work(self): # Создаем фунцию
		while True: #Функция бесконечна 
			sleep(1) #Засыпание на 1 секунду

	def speak(self): #Создаем еще 1 функцию
		print(self.favorite_phrase) #Выводим переменную , описывающую класс

man = Typical_dag_05() #Присваем описание класса переменной 
print(man.iq) #Выводим описание класса
man.favorite_phrase = 'Mom, give me money, please.' #Изменяется описание переменной 

man.speak() #Задействуем функцию
