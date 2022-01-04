# def

nevek1 = ['Yena', 'Böszi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Evi', 10, True]
nevek2 = ['Pityu', 'Ati', 'Peti', 'Bence', 'Feri']

#for nev in nevek1:
#    print(nev)

def nev_print(nev_lsita):
    for nev in nev_lsita:
        if isinstance(nev, str):
            print(nev.upper()) #Nagybatüssé teszem a neveket!
        else:
            print("Nem string tipusú, hanem: " + str(type(nev)))

nev_print(nevek1)
nev_print(nevek2)
