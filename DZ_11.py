
print ("""Хеллоу , я универсальный робот
Фильтратор версия 228 и сейчас я задам тебе пару вопросов 
Которые определят твою дальнейшую судьбу,итак ,начнем """)
earnings=int(input("""Твой заработок больше 1000 биткоинов в час ?
1=Да 0=Нет 
"""))
if earnings==0:
	print ("Вы нам не подходите , такие как Nevesta_name на дороге не валяются")
if earnings==1:
	home=int(input("""Итак , пока вроде все хорошо , но есть еще вопросы.
Площадь дома больше чем 1к кв. метров ?
1=Да 0=Нет
"""))
	if home==0:
		print ("Вы нам не подходите , такие как Nevesta_name на дороге не валяются")
	if home==1:
		car=int(input("""Расстояние от дна твое машины до пола меньше 1мм?
1=Да 0=Нет
"""))
		if car==0:
			print ("Вы нам не подходите , такие как Nevesta_name на дороге не валяются")
		if car==1:
			guests=int(input("""Все прекрасно , остался последний вопрос.
На свадьбе будет больше 1кк людей ?
1=Да 0=Нет
"""))
			if guests==0:
				print ("Вы нам не подходите , такие как Nevesta_name на дороге не валяются")
			if guests==1:
				print ("Прекрасно , вы прошли по всем параметрам ,вы нам подходите !!!")
					
	

