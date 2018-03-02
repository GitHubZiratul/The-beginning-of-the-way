from time import sleep
from random import randint
class Doter ():
	favorite_phrase='Ну ,мам, еще 5 минут'
	girlfriend=None
	friends=None
	skill=True
	strength=1
	agility=5
	intellect=3
	boyfriend=None
	money=None
	
	def mamka_oret(s):
		print (s.favorite_phrase)
	def played_until_the_morning(s):
		while True:
			sleep (2)
	def go_to_the_gym(s):
		boyfriend=True
		strength=strength+8
		print ('Протеин , Миша МавашЫ ЫЫЫЫЫЫЫЫ	')
	def went_outside(s):
		friends=True
		agility=agility+3
		print ('Поздравляю , ты нашел себе друзей')
	def go_to_the_library(s):
		intellect=intellect+7
		print ('Твой словарный запас пополнен')
	def get_a_job (s):
		girlfriend=True
		money=True
		print ('Поздравляю у тебя появились деньги и девушка, но ты больше не дотер')
shkolnik = Doter()
n=int(input('''Что будещ делать , задр ? 
	1-Ответить маман
	2-Лечь спать 
	3-Пойти в тренажерный 
	4-Погулять
	5-В библиотеку
	6-Найти работу'''))
if n==1:
shkolnik.mamka_oret()



			




