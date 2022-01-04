# exception handling (error handling) - kivételkezelés (hiakezelés)

lista = [1,2,3]

try:
    print(lista[5])
    #print(askd)
    #print(1/0)
except NameError as e:
    print(e, '- Nem létező változó!')
except IndexError as e:
    print(e, '- Tartományon kívüli indexelés!')
except ZeroDivisionError as e:
    print(e, '- 0-val osztán nem lehetséges!')
    print('A program vége!')

#lista = ['1', '2', '3', None, '4', '', '5', True, 'Bozsi', '12.65']
#
#for i in lista:
#    try:
#        print(int(i)*2)
#    except:
#        continue


#try: #csak 1 lehet ebből
#    print('bla')
#except: #Bármennyi lehet ebből
#    print('Nem létező változó!')
#else: #csak 1 lehet ebből
#    print('az else')
#finally: #csak 1 lehet ebből
#    print('try vége')