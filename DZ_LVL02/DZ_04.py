teammates=0
while True:
	
	palyer= {}

	
	palyer['Name']=input ('Как вас зовут ?')
	palyer['Mathematics']=int(input("""Какая у вас оценка по математике?
								"""))
	if palyer['Mathematics'] >=6:
		print ('Пшел вон отсюда , обманщик')
		continue 
	palyer['Physics']=int(input("""Какая у вас оценка по физике?
								"""))
	
	if  palyer['Physics'] >=6:
		print ('Пшел вон отсюда , обманщик')
		continue 
	palyer['Chemistry']=int(input("""Какая у вас оценка по химии?
								"""))
	if  palyer['Chemistry'] >=6:
		print ('Пшел вон отсюда , обманщик')
		continue 
	palyer['Biology']=int(input("""Какая у вас оценка по биологии?
								"""))
	if  palyer['Biology'] >=6:
		print ('Пшел вон отсюда , обманщик')
		continue 
	palyer['Geography']=int(input("""Какая у вас оценка по географии?
								"""))
	if palyer['Geography']>=6:
		print ('Пшел вон отсюда , обманщик')
		continue 
	if (palyer['Mathematics']+palyer['Physics']+palyer['Chemistry']+palyer['Biology']+palyer['Geography'])/5>=4.8:
		teammates+=1
		print ('Поздравляю',palyer['Name'],',вы в комманде')
		if teammates==3:
			print ('Комманда укомплектована')
			break			
	elif (palyer['Mathematics']+palyer['Physics']+palyer['Chemistry']+palyer['Biology']+palyer['Geography'])/5<4.8:
		print ('К сожалению',palyer['Name'],',вы не проходите')
