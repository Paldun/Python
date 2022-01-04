#lists - listák/lista


lista1 = ['Balázs', 'Anikó', 'Zsolti', 'Szabina', 'Ildi']

print(lista1[0]) #Az adott helyen lévő adatot lehet vele kiválasztani! Más néven indexelésnek nevezzük.
print(lista1[-1]) #A legutolsó elemet irattassuk ki!

print(lista1[0:3]) #A szeleteléssel egy adott adattól lehet elmenni egy másik adatig!
print(lista1[2:]) #A 2-től a végéig iratattom ki!
print(lista1[:4]) #A 4-től az eleéig iratattom ki!

tartomany = range(101) #valamettől valameddig
print(list(tartomany))


#multi dimensionol lists - több dimenziós lista

lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista2[0]) #1 lista kiirattatása
print(lista2[1]) #2 lista kiirattatása
print(lista2[2]) #3 lista kiirattatása

print(lista2[2][2]) #A 3. listából az utolsó elemet irattaom ki! 
print(lista2[0][1]) #A 1. listából az második elemet irattaom ki! 
print(lista2[1][1]) #A 2. listából az második elemet irattaom ki! 

