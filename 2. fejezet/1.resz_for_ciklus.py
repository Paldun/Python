#for loop - for ciklus

for i in range(10): #10x kiirattatom a Helló! szöveget
    print('Helló!')

lista1 = ['Balázs', 'Anikó', 'Zsolti', 'Szabina', 'Ildi']

for i in range(len(lista1)): #Az i-nek megadom a lista hosszúságát, és kiiratatom a listának az összes tagját eggyesével.
    print(lista1[i])

for i in lista1:
    print(i)