# Игра в кости
# 1.Играют два человека
# 2.У каждого есть запас денег
# 3.В начале игры каждый делает ставку 
# 4.Затем подбрасываеются кубики
# 5.Тот , у кого больше очков , вин
# 6. Игра до конца
import random
player_1={ 'Score':10000}
player_2={ 'Score':10000}
player_1['Name']=input ('Игрок№1 , как вас зовут? ')
player_2['Name']=input ('Игрок№2 , как вас зовут? ')
while  True:
	player_1['Rate']= int(input('Первый игрок , ваша ставка?'))
	player_2['Rate']= int(input('Второй игрок , ваша ставка?'))

	player_1['Cast']=random.randint(2,12)
	player_2['Cast']=random.randint(2,12)

	print('Первый игрок , ваш бросок(бросает ,выпадает)',player_1['Cast'],'очков')
	print('Второй игрок , ваш бросок(бросает ,выпадает)',player_2['Cast'],'очков')
	if player_1['Rate']> player_1['Score']:
		print (player_2['Name'],'ваша сдытавка превышает счет')
		break
	if player_2['Rate']> player_2['Score']:
		print (player_2['Name'],',ваша ставка превышает счет')
		break
	if player_1['Cast']>player_2['Cast']:
		print ('Первый игрок сорвал куш')
		player_1['Score']+= player_2['Rate']
		player_2['Score']-=player_2['Rate']
	if player_2['Cast']>player_1['Cast']:
		print ('Второй игрок сорвал куш')
		player_2['Score']+= player_1['Rate']
		player_1['Score']-=player_1['Rate']	
	else:
		print ('Ничья')

	print('У первого игрока на счету ',player_1['Score'])
	print('У второго игрока на счету ',player_2['Score'])
	if player_1['Score']<=0:
		print("Денег нет , иди к банкомату,бомж .",player_1['Name'],",вы банкрот")
		break 
	if player_2['Score']<=0:
		print("Денег нет , иди к банкомату,бомж .",player_2['Name'],",вы банкрот")
		break 
	