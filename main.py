def citireLista():
    list = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        list.append(int(input("Dati elemente: ")))

    return list



def numerenegative(list):
    """
    Determina numerele negative nenule din lista
    :param list: numere intregi
    :return: numerele negative nenule
    """
    rezultat=[]
    for i in list:
        if i<0:
            rezultat.append(i)
    return rezultat

def test_numrenegative():
    assert (numerenegative([1,2,3,4,5])==[])
    assert (numerenegative([-1,2,3,-4])==[-1,-4])
    assert (numerenegative([1,-2,3,4])==[-2])



def celmaimicnrcuultimacifradata(list,n):
    """
    Determina cel mai mic numar care are ultima cifra egala cu o cifra introdusa de la tastatura
    :param list:numere integi
    :param n:numar integ
    :return:cel mai mic numar care are ultima cifra egala cu o cifra introdusa de la tastatura
    """
    list.sort()
    for i in list:
        if i%10==n:
            return i

def test_celmaimicnrcuultimacifradata():
    assert (celmaimicnrcuultimacifradata([1,6,34,68,40,48,20],8)==48)
    assert (celmaimicnrcuultimacifradata([1,26,36,4,5],6)==26)
    assert (celmaimicnrcuultimacifradata([1, 25, 36, 55, 5], 5) == 5)



def numarprim(x):
    """
    Determina daca un numar este prim
    :param x: numer intreg
    :return: daca numarul este prim sau nu
    """
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False

    return True

def cifreprime(n):
    """
    Determina daca toate cifrele unui numar sunt prime
    :param n: numar intreg
    :return: True daca toate cifrele sunt prime, iar in caz contrar False
    """
    while n!=0:
        cifra=n%10
        if numarprim(cifra) == False:
            return False
        n=n//10
    return True

def superprim(list):
    """
    Determina daca toate numerele din lista in caare toate cifrele numerelor sunt numere pare
    :param list: numere intregi
    :return: numerele care au toate cifrele numere prime
    """
    rezultat=[]
    for i in list:
        if cifreprime(i) == True:
            rezultat.append(i)
    return rezultat

def test_superprim():
    assert (superprim([173,235])==[235])
    assert (superprim([123,456,567])==[])
    assert (superprim([235,357,573])==[235,357,573])



def cmmdcauneiliste(list):
    """
    Determina cmmdc a numerelor dintr-o lista
    :param list: numere intregi
    :return: cmmdc-ul numerelor
    """
    d=0
    for i in list:
        imp=i
        while imp!=0:
            r=d%imp
            d=imp
            imp=r
    return d

def invernumarnegativ(n):
    """
    Determina oglinditul unui numar negativ
    :param n: numar intreg
    :return: oglinditul numarului
    """
    ogl=0
    nr=abs(n)
    while nr>0:
        ogl=ogl*10+nr%10
        nr=nr//10
    return -ogl

def numerepoznumereneg(list):
    """
    Determina o lista in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul lor , iar numerele negative cu cifrele in ordine inversa
    :param list: numere intregi
    :return: lista in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul lor, iar numerele negative cu cifrele in ordine inversa
    """
    rez=[]
    poz=[]
    for i in list:
        if i>=0:
            poz.append(i)
    cmmdc=cmmdcauneiliste(poz)
    for i in list:
        if i>=0:
            rez.append(cmmdc)
        else:
            invers=invernumarnegativ(i)
            rez.append(invers)
    return rez

def test_numerepoznumereneg():
    assert (numerepoznumereneg([-76,12,24,-13,144])==[-67,12,12,-31,12])
    assert (numerepoznumereneg([-12,-13,-14,-15])==[-21,-31,-41,-51])
    assert (numerepoznumereneg([12,14,16,18])==[2,2,2,2])



def main():
    test_numrenegative()
    test_celmaimicnrcuultimacifradata()
    test_superprim()
    test_numerepoznumereneg()
    l=[]
    while True:
        print("1. Citire lista: ")
        print("2. Afisarea tuturor numerelor negative nenule din lista")
        print("3. Afiseaza cel mai mic numar care are ultima cifra egala cu o cifra introdusa de la tastatura")
        print("4. Afiseaza toate numerele din lista in caare toate cifrele numerelor sunt numere prime")
        print("5. Afiseaza o lista in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul lor , iar numerele negative cu cifrele in ordine inversa")
        print("a. Afisare lista")
        print("x.Inchide")
        optiune=input("dati op: ")
        if optiune=="1":
            l=citireLista()
        elif optiune=="2":
           print(numerenegative(l))
        elif optiune=="3":
            n=int(input("Dati nunmarul cu care vreti sa fie egal ultima cifra: "))
            print(celmaimicnrcuultimacifradata(l,n))
        elif optiune=="4":
            print(superprim(l))
        elif optiune=="5":
            print(numerepoznumereneg(l))
        elif optiune=="a":
            print(l)
        elif optiune=="x":
            break
        else:
            print("reinc")

if __name__ == '__main__':
    main()