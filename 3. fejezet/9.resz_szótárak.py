# Dictionaries, key-value pairs - Szótárak, kulcs-érték parosok

nev_kor = {'Ili':28, 'Betti':37, 'Magdi':41, 'Ani':34}
#          {kucs:érték, stb}

nev_kor['Andi'] = 56 #Így lehet hozzáadni újabb értéket.
print(nev_kor)

nev_kor.pop('Ili') #Így lehet törölni az értéket és a kucsot is.
print(nev_kor)

print(nev_kor.get('Ani')) #A szótárban lévő adott értéket lehet lekérdezni!

nev_kor2 = {'Ili':{'kor':28, 'hajszín':'szőke'},
            'Betti':{'kor':37, 'hajszín':'barna'},
            'Magdi':{'kor':41, 'hajszín':'fekete'},
            'Ani':{'kor':34, 'hajszín':'vörös'}}

for key in nev_kor.keys(): # A ciklussal most CSAK a kulcsot (key-t) printelem ki!
    print(key)

for value in nev_kor.values(): # Míg ennél CSAK az értéket (value-t) printelem ki!
    print(value)

for key, value in nev_kor.items(): # Itt mind a két adatot kiíratom! (key, value)
    print(key, value)

dict1 = {'adat1':[1,2,3,4,5,6], 'adat':78, 'adat3':(9,8,7,5)}