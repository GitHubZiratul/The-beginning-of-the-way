
game_worlds= ['Elders Scrolls','Warcraft',
'Gothic','Grand Theft Auto','Fallout','Diablo','Dishonored']
print ("Вот ваш список",game_worlds)
while True:
	a=input("""Что будете делать со списком?
	""")
	if a== ('Ничего'):
		print ('Вот ваш список',game_worlds)
		break
	if a==('Добавить элемент'):
		b=input ("""Куда будем добавлять элемент ? 
		""")
		if b==('В конец'):
			c=input("""Что хотите добавить в конец ? 
			""")
			game_worlds.append(c)
			print(game_worlds)
		else:
			c=int(input("""Что хотите добавить?"""))
			game_worlds.insert(b, c)
			print (game_worlds)
	elif a==('Удалить элемент'):
		q=input("""Как вам легче удалить элемент по значению или по индексу ?
		 """)
		if q==('По значению'):
			w=input("""Какое слово вы хотите удалить ? 
		 """)
			game_worlds.remove(w)
			print (game_worlds)
		if q==('По индексу'):
			e=int(input("Введите индекс"))
			del game_worlds[e]
			print (game_worlds)
	if a==('Очистить список'):
		game_worlds.clear()
		print (game_worlds)
	if a==('Скопировать список'):
		game_worlds_copy=game_worlds[:]
	