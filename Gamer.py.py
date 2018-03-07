from time import sleep
class Gamer:
	reputation=10
	acidity=None
	average_age=15
	love_of_other_peoples_moms=None
	poise=True
	favorite_phrase ='Еще 5 минут'
	def no_work(self): 
		while True: 
			sleep(1)
	def speak(self):
		print(self.favorite_phrase)
	
Doter=Gamer()
Doter.reputation=5
Doter.acidity=True
Doter.average_age=12
Doter.love_of_other_peoples_moms=True
Doter.poise=None
Doter.favorite_phrase ='НЫЫЫЫА , ОЧЕРЕДНЯРА'



CS_Player=Gamer()
CS_Player.reputation=7
CS_Player.average_age=13
CS_Player.favorite_phrase ='Easy,Peasy,Lemon Squeezy '


Minecraft_player=Gamer()
Minecraft_player.reputation=3
Minecraft_player.average_age=8
Minecraft_player.poise=None
Minecraft_player.love_of_other_peoples_moms=True
Minecraft_player.favorite_phrase ='Я видео записываю , скажЫ  прифет ютубу'


PUBG_Player=Gamer()
PUBG_Player.reputation=9
PUBG_Player.average_age=15
PUBG_Player.favorite_phrase ='Опять каряк '

Doter.speak()
CS_Player.speak()

