m=int(input('Сколько часов в день вы работаете ?'))
age=20
while True:
	m+=1
	if m>=18:
		print ("""С 20 лет  вы работали в этом месте 
			с каждым месяцем увеличивая свой рабочий день на 5 минут.
			В итоге вы не выдержали всей этой нагрузки
			Вы умерли от переутомления в возрасте""",age,'лет')
		break

	age+=1
	