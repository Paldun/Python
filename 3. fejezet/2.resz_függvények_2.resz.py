a = 10
b = 20

def osszeadas():
    print(a + b)

def osszeadas2(a, b, c=4):
    return a + b + c


def osszeadas3(*args):
    return sum(args)


def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for i in args:
        koszones += i
        koszones += ", "
    print(koszones[0:len(koszones)-2])

udvozlesek('szia', 'szevasz', 'hello', 'szervusz')

#osszeadas()
#print(osszeadas2(32,53))
#print(osszeadas3(10,20,30,40,50,60,70,80,90,100))