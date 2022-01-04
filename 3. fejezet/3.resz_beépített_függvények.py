#Beépített függvények

print(abs(-78)) #a szám abszolút értékét adja meg

nevek1 = ['Yena', 'Böszi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Evi']
for index, nev in enumerate(nevek1): #Megszámozom a neveket!
    print(index, nev)

print(float(10))

print(hex(125)) #Egy adott szám hexadecimális értékét adja meg

print(int(24.65)) #egész számmá konvertálja át

print(max(7,4,78,23,123)) #A legnagyobb ártékat vállasztja ki
print(min(7,4,78,23,123)) #A legkissebb számot adja vissza.

print(pow(2, 10)) #A hatványozás egyszerübb módja **

print(list(reversed(nevek1))) #Megfordítja a lista tartalmát

print(round(16.455)) #Kerekiti a számokat
print(round(16.526))
print(round(16.4552623, 2)) #A tizedes pont utáni számig írja ki