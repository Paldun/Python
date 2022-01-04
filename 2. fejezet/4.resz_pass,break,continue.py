# pass, break, continue

#while True:
#    pass #A pass-sel helyetesíted azt a kódot amit még nem találtál ki!

for i in range(10):
    if i == 5:
        break
    print(i)

szam = 0

while True:
    print(szam)
    if szam == 6:
        break #A break leállítja az adott loopot
    szam += 1

for i in range(10):
    if i == 5:
        continue #A continue átugrik a következő loopra
    print(i)

szamlalo = 0

while True:
    szamlalo += 1
    if szamlalo % 2 == 0:
        continue
    print(szamlalo)
    if szamlalo > 20:
        break