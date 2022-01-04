#lists - listák/lista

lista1 = []

print(lista1)

lista1.append(100)
lista1.append(101)
lista1.append(102) #A listához így lehet valamit hozzáadni. Szöveget a macskaköröm segítségével tudod hozzáadni. ("")
lista1.append(103)
lista1.append(104)

print(lista1)

lista1.append('Ádám')
lista1.append('asdasd') #A listához stringet is hozzá lehet adni nem csak intiger-t!
lista1.append('asda')

print(lista1)

lista1.remove('asda') #Ezzel törölni lehet egy adott szót/számot!

print(lista1)

#lista1.clear() #A listát teljesen törli!

#print(lista1)

lista1.insert(5, 'szöveg') #Beszúrok a listába egy adott szöveget/számot!

print(lista1)

lista1.reverse() # Az egész lista tartalmát megfordítja!

print(lista1)


lista2 = [15, 8 ,78, 23, 1, 65, 184]
lista2.sort() #Növekvő sorrendbe rakja a számokat. Figyelem!!! A intigerekhez NEM lehet hozzáadni stringet mert nem tudja összehasonlítani a szót a számmal!
print(lista2)

lista3 = ['Balázs', 'Anikó', 'Zsolti', 'Szabina']
lista3.sort() #Abc sorrendbe rakja a neveket. Figyelem!!! A stringhez NEM lehet hozzáadni intigereket mert nem tudja összehasonlítani a szót a számmal!
print(lista3)

print(len(lista3)) #a listákban található adatok összességét írja ki!