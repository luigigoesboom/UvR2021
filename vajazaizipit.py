import math
import random

def naloga1(f):
    c = 5/9 * (f-32)
    print (c)    

def naloga3(hitrost,kot):
    
    return ((hitrost**2)*math.sin(2*math.radians(kot)) / 10)


def naloga5():
    a = random.randint(2,10)
    b = random.randint(2,10)
    print(a, " krat ", b)
    c = int(input("Odgovor?"))
    if (c == a * b):
        print("Pravilno!")
    else:
        print("Napačno")

def naloga7():
    st = int(input("Število izdelkov:"))
    cena = 0
    i = 0
    while i < st:
        cena += int(input("Cena izdelka:"))
        i += 1
    print("Vsota:", cena)    

def naloga9():
    st = int(input("Število izdelkov:"))
    cena = 0
    i = 0
    while i < st:
        cena += int(input("Cena izdelka:"))
        i += 1
    print("Vsota:", cena)
    print(cena/st)
    
def naloga11():
    def vrzi():
        return random.choice("GC")
    
    kovanci = 5
    
    while kovanci > 0 and kovanci < 10:
        met = vrzi()
        if met == "G":
            kovanci -= 1
        else:
            kovanci += 1
        print(met, kovanci)

def naloga13():
    stev = int(input("Vpiši št:"))
    while (stev%10) > 0:
        print((stev%10))
        stev = stev//10
        
def naloga15(v1,v2,oper):
    if oper == "*":
        print (v1*v2)
    elif oper == "+":
        print(v1+v2)
    elif oper == "-":
        print(v1-v2)
        
def naloga17(beseda, znak):
    return (beseda.count(znak))

def naloga19(s):
    najvecji = s[0]
    for i in s:
        if i < 0:
            i = i*-1
        
        if i > najvecji:
            najvecji = i
    return najvecji

def naloga21(niz):
    najdaljsa = ""
    for x in niz.split():
        if len(x) > len(najdaljsa):
            najdaljsa = x
            
    return najdaljsa

def naloga23(s):
    s.sort()
    i = 1
    teza = 0
    while i < len(s)-1:
        teza += s[i]
        i+=1
    print (teza/len(s)-2)
    
def naloga25(s):
    a = False
    for x in s:
        if x % 2 == 1:
            a = True
    return a

def naloga27(s):
    vrsta = 0
    najdalsa = 0
    for x in list(s):
        if x == "+":
            vrsta += 1
        else:
            vrsta -= 1
        if vrsta > najdalsa:
            najdalsa = vrsta
    return(najdalsa)

def naloga29(x):
    i = 1
    while i <= x:
        if x % i == 0:
            print (i)
        i += 1
        
def naloga31(x):
    i = 1
    ses = 0
    while i < x:
        if x % i == 0:
            ses += i
        i += 1
    return(ses)
    
def naloga33():
    for i in range(1,1000):
        if i == naloga31(i):
            print(i)

def naloga35(n):
    a = False
    for z in list(str(n)):
        if int(z) == 7:
            a = True
    return (a)

def naloga37():
    i = 2
    fib = [1,1]
    while i < 20:
        fib.append(fib[i-1] + fib[i-2])
        i+= 1
    for x in fib:
        print (x)
    
naloga37()