i=int(input('Введите число'))
sum_chet=0
sum_nechet=0
while True:
    i = i // 10 
    if i%2==0:
        sum_chet=sum_chet+i
    if i%2 !=0:
        sum_nechet=sum_nechet+i
    if i==0:
        break

if sum_chet>sum_nechet:
        print ('+')
        
if sum_chet<sum_nechet:
        print ('-')
        
    
     
    