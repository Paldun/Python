jelszo = 'kisuborka'
proba = 0
bemenet = input("Mi a jelszó? ")

while bemenet != jelszo:
    proba += 1
    if proba == 2:
        print("Hozzáférés megtagadva!")
        break
    print("Rossz jelszó, próbáld újra!\n")
    bemenet = input("Mi a jelszó? ")

if bemenet == jelszo:
    print("Hozzáférés sikeres!")