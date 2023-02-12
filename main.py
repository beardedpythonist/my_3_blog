import sqlite3

# поиск по марке
Mercedec = ['mercedes','Mercedes', 'Merc', 'мерс', 'MERCEDES', 'MERC','мерседес', 'Мерседес','Мерс', 'МЕРСЕДЕС']
BMW = ['BMW','Bmw','bmw', 'БМВ','Бмв',',бмв']
Land = ['Land Rover','LAND ROVER','Land','Ленд Ровер','Ленд','Ланд Ровер',]
volvo =['Volvo', 'VOLVO','Вольво','ВОЛЬВО']
audi =['Audi','AUDI','ауди','Ауди','АУДИ']
vw =['Volkswagen''VOLKSWAGEN''VW''фольксваген''Фольксваген''ФОЛЬСКВАГЕН']
ford = ['Ford','FORD','ford','форд','Форд','ФОРД']
Jaguar = ['Jaguar','JAGUAR','ягуар','Ягуар','ЯГУАР']
poisk = input('введите марку авто: ')
slov = {'Mercedes':['mercedes','Mercedes', 'Merc', 'MERCEDES', 'мерс',
                            'MERC','мерседес', 'Мерседес','Мерс', 'МЕРСЕДЕС'],
        'BMW':['BMW','Bmw','bmw', 'БМВ','Бмв','бмв'],
        'Land': ['Land Rover','LAND ROVER','Land','Ленд Ровер','Ленд','Ланд Ровер'],
        'volvo': ['Volvo', 'VOLVO','Вольво','ВОЛЬВО'],
        'audi' :['Audi','AUDI','ауди','Ауди','АУДИ'],
        'vw' :['Volkswagen','VOLKSWAGEN','VW','фольксваген','Фольксваген','ФОЛЬСКВАГЕН'],
        'ford' : ['Ford','FORD','ford','форд','Форд','ФОРД'],
        'Jaguar' : ['Jaguar','JAGUAR','ягуар','Ягуар','ЯГУАР']}

flag = False
for key, val in slov.items():
    if poisk in val:
        print(key)
        flag = True
        break


if not flag:
    print('Машина не найдена')



# with  sqlite3.connect('mydb.db') as mojabaza:
#     cursor = mojabaza.cursor()
#     cursor.execute(" SELECT * FROM myDB")
#     for c in cursor:
#         if x in c[2]:
#             print(c)
