a=1
b=0
n=0
f=int(input('Сколько чисел Фибоначчи вы хотите вывести ?'))
print (b)
while True:	
	a=a+b
	n+=1
	print (a)
	if n>=f:
		break
	b=a+b
	n+=1
	if n>=f:
		break
	print (b)
	
	