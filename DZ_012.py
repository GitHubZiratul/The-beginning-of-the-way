import time
text_Navalnyi=input ("""Введите вашу статью """)
print (
	"""
Модератор обрабатывает данные , пожалуйста подождите

	""")
time.sleep(5)
print ("Текст прощел обработку , вот весь Текст")
print(text_Navalnyi.replace('коррупция', '***').replace('коррупционных','***').replace('корупцией','***').replace('коррупции','***'))