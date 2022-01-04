# if elágazódás

eletkor = 17

if eletkor < 18:
    if eletkor >= 16:
        print('Egy kis sört megihatsz!')
    else:
        print("Se cigi, se pia!")
elif eletkor >= 18 and eletkor < 30:
    print("Jó bulizást!")
elif eletkor > 30 and eletkor < 65:
    print("Munka és család.")
else:
    print("Nyugdijas élet, meg unokák!")