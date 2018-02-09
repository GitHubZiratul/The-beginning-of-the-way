team=input('Состав вашей комманды')
team= team.split(' ')
team1 =input('Состав комманды после тестирования')
team1= team1.split(' ')
i=0
while  True:
	if team[i] in team1:
		print(team[i])
		
	else:
		i+=1
	



	

