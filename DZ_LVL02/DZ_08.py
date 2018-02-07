n = int(input('Введите ваше число'))
summa=0
while n>0:	
	summa=summa + n%10
	n = n // 10 
print("Сумма цифр:", summa)
