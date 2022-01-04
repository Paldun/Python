#f = open('3. fejezet/5.res_mondasok.txt', 'r', encoding='utf-8')
#
#for sor in f:
#        print(sor.strip())
#
#f.close()

with open('3. fejezet/5.res_mondasok.txt', 'r', encoding='utf-8') as file:
    sor = file.readline() #1 sort olvas be egyszerre
    print(sor)

    #while sor: #A while ciklus azért kell hogy amíg talál sort a file-ban addig suttasa a program!
    #    print(sor.strip())
    #    sor = file.readline()

    sor = file.readlines() #Listába teszi a sorokat, ezzel olvassa be.
    print(sor)

    sor = file.read() #Az egész filet beolvassa. De ez csak kevés soros fileokon érdemes használni. 100 sorig érdemes használni.
    print(sor)