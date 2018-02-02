dictionary= {
    'man':'мужЫк',
    'woman':'женщина',
    'boy':'мальчик',
    'girl':'девочка',
    'boss':'босс',
    'cat':'кошка',
    'dog':'собака',
}
print (dictionary)
c1=input ("""Что вы хотите сделать ?
     1-Добавить слово 
     2-Удалить слово 
     3-Перевести слово
            """)
if c1==('1'):
    orig=input("""Введите слово на анг
            """)
    tr=input("""Введите слово на рус
            """)
    dictionary[orig]=tr
    print (dictionary)
elif c1==('3'):
    a=input("""Какое слово вы хотите найти ?
            """)
    a=dictionary[a]
    print (a)
elif c1==('2'):
    q=input("""Введите слово , которое вы хотите удалить ? 
            """)
    del dictionary[q]
    print (dictionary)
     