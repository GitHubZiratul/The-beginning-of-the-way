import random 

score=500
while True:
	cost_eth=random.randint(1,100)
	cost_btc=random.randint(1,100)
	cost_eth_2=random.randint(1,100)
	cost_btc_2=random.randint(1,100)
	print("""Стоимость Ethereum=""",cost_eth,
		"""Стоимость Bitcoin=""",cost_btc,
		)
	way=int(input("""Что будем покупать ?
		1-Ethereum
		2-Bitcoin
		3-И то и другое
		"""))
	if way==1:
		quantity_eth=int(input("""Какое количество вы хотите купить ?
			"""))
		score=score-quantity_eth*cost_eth
		print ('Ок,прошла неделя и теперь курс=',cost_eth_2)
		score=score+quantity_eth*cost_eth_2
		print ('Ваш счет=',score)

		if quantity_eth*cost_eth>score:
			print ("Вам нехватает денег")
	if way==2:
		quantity_btc=int(input("""Какое количество вы хотите купить ?
			"""))
		score=score-quantity_btc*cost_btc
		print ('Ок,прошла неделя и теперь курс=',cost_btc_2)
		score=score+quantity_btc*cost_btc_2
		print ('Ваш счет=',score)

		if quantity_btc*cost_btc>score:
			print ("Вам нехватает денег")
	if way==3:
		quantity_all=int(input('Какое количество вы хотите купить ?'))
		score=score-((quantity_all*cost_btc)+(quantity_all*cost_eth))
		print ('Ок,прошла неделя и теперь курс Биткоина=',cost_btc_2)
		print ('Ок,прошла неделя и теперь курс Эфириума=',cost_eth_2)
		score=score-((quantity_all*cost_btc_2)+(quantity_all*cost_eth_2))
		print ('Ваш счет=',score)
	if score==0:
		print ('Вам нехватает денег')
		break
	if score<cost_btc:
		print ('Вам нехватает денег')
		break
	if score<cost_eth:
		print ('Вам нехватает денег')
		break
	if score>=1000:
		print ('Вы достигли поставленной цели , боздравляю')
		break
		

		