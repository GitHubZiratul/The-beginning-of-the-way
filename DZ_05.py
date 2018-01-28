weight= float(input("Введите свой вес"))
height= float(input("Свой рост"))
age= float(input("Возраст"))
ind=float(weight/height**2)
if 1 < age < 25:
    if ind<17.5:
        print ("Недостаток,опасно для здоровья ")
    if 22.9>ind>19.5:
        print ("Слегка сниже , неопасно для здоровья")
    if 19.5<ind<22.9:
        print ("Норма")
    if 27.4>ind>23.0:
        print ("Излишний")
    if 29.9>ind>27.5:
        print ("Ожирение 1степень")
    if 34.9>ind>30:
        print ("Ожирение 2 степень")
    if 39.9>ind>35:
        print ("Ожирение 3 степень")
    if ind>40.:
        print ("Ожирение 4 степень")
if  26 < age < 100:
    if ind<18:
        print ("Недостаток,опасно для здоровья ")
    elif 18<ind<20:
        print ("Норма")
    elif 20<ind<25.9:
        print ("Cлегка снижен , неопасно для здоровья")
    elif 25.9<ind<27.9:
        print ("Излишний")
    elif 28<ind<31:
        print ("Ожирение 1степень")
    elif 31<ind<36:
        print ("Ожирение 2 степень")
    elif 36<ind<41:
        print ("Ожирение 3 степень")
    elif ind>41:
        print ("Ожирение 4 степень")
    
    
    
