# tuple - nem modosítható adathalmaz (immutable)

# modositható adat []
lista = ['Juci', 'Ani', 'Ildi', 'Barbi', 'Szabina']

# nem modosítható adat ()
tup1 = ('Juci', 'Ani', 'Ildi', 'Barbi', 'Szabina',  'Barbi', 'Barbi', 'Barbi')

print(tup1.index('Ildi'))# Megadja hogy hanyadik helyen áll
print(tup1.count('Barbi')) # Megszámolja az adott adatot

#lista.append('Bözsi')
#print(lista)
#
#lista[-1] = 'Betti'
#print(lista)

# tup1[-1] = 'Bözsi' # <--- Ezt nem tudja végrehajtani a python mert, NEM modosítható a tuple

# print(tup1[2]) #lehet szelelni, indexelni

#tup2 = tuple(lista) # lista > tuple
#print(tup2)
#
#lista2 = list(tup2) # tupple > lista
#print(lista2)