# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a'  = append (hozzáfűzés, mellékel)


with open('python/3. fejezet/5.res_mondasok.txt', 'r', encoding='utf-8') as infile:
    with open('python/3. fejezet/6.resz_iras.txt', 'w+', encoding='utf-8') as outfile:

        sor = infile.readline()
        while sor:
            outfile.write(sor)
            sor = infile.readline()


#with open('python/3. fejezet/6.resz_iras.txt', 'a', encoding='utf-8') as file:
#    ujsor = '\n6.resz_iras.txt'
#    file.write(ujsor)