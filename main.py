import sqlite3


merc = ['mercedes','Mercedes', 'Merc', 'MERCEDES', 'MERC','мерседес', 'Мерседес','Мерс', 'МЕРСЕДЕС']
BMW = ['BMW','Bmw','bmw', 'БМВ','Бмв']
Land = ['Land Rover','LAND ROVER','Land','Ленд Ровер','Ленд','Ланд Ровер',]
volvo =['Volvo', 'VOLVO','Вольво','ВОЛЬВО']
audi =['Audi','AUDI','ауди','Ауди','АУДИ']
vw =['Volkswagen''VOLKSWAGEN''VW''фольксваген''Фольксваген''ФОЛЬСКВАГЕН']
ford = ['Ford','FORD','ford','форд','Форд','ФОРД']
jag = ['Jaguar','JAGUAR','ягуар','Ягуар','ЯГУАР']

poisk = input('введите марку авто: ')
slov ={'merc':['mercedes','Mercedes', 'Merc', 'MERCEDES', 'MERC','мерседес', 'Мерседес','Мерс', 'МЕРСЕДЕС'],
       'BMW': ['BMW','Bmw','bmw', 'БМВ','Бмв']}
for key, val in slov.items():
    if poisk in val:
        x = key

with  sqlite3.connect('mydb.db') as mojabaza:
    cursor = mojabaza.cursor()
    cursor.execute(" SELECT * FROM myDB WHERE model like '%?%' ", ('x'))
    for c in cursor:
        print(c)
