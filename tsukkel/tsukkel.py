
from random import *


##n 11
a=0

#n=randint(1,10)
#while True:
#    text = input("Väljumiseks sisestage number : ")
#    a+=1
#    if text == "stopp":
#        print("Välju programmist! Kohtumiseni! See sai tehtud", n)
#        break # инструкция выхода из цикла
#    elif int(text) == n:
#        print("palju õnne, sa võitsid")
#        break
#    else:
#        print("proovi veel korra")
#    if a == 3:
#        print("3 katset ammendatud")
#        break

##10
n=0
while True:
    if n>100:
        break
    elif n%5==0:
        print(n, end=" ")
    n+=1
    

                            ##16
#ans = random.randint(1, 10)
#while True:
#    g=input("mis numbri ma arvasin? (1-10, mangu lõpetamiseks kirjutage *lõpp*)")
#    if g.lower() == "lõpp":
#        print("mäng on läbi")
#        break
#    if not g.isnumeric():
#        print("vale andmetüüp")
#        continue
#    g = int(g)
#    if g == ans:
#        print("õige! sa arvaside ära ")
#        break
#    if g>10 or g<1:
#        print("Vahemik on vale!")
#        continue
#    elif g !=ans:
#        print("vale!proovi veel korra! numbri oli {ans}" )
        


        ##3
 
#try:
#    f=int(input("mitu ülesandeid sa tahad?"))
#    for d in range (0,f,1):
#        print(f"ülesanne{g}:")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a + b
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print("see on õige")
#                break
#            else:
#                print("proovi veel korra")
#                print()
#        g = g+1
#        print(f"õige on {c}")
#except:
#    print("see ei ole õige")
#####13
#print("arv","   ruut", "    kuup")
#for i in range(1,11):
##    print( i , i**2 , i**3 )
#    print(f" {i}    {i ** 2}     {i ** 3}")
 


#import string
#import random
##0
# print("Arva täht - (Aa kuni Zz)")
# täht = random.choice(string.ascii_letters)
# while True:
#     answ = str(input("Teie oletus"))
#     if täht==answ:
#        print("tubli")
#        break
# else: print("proovi uuesti!")


##22
#while True:
#    print("Tahan kommi!")
#    a = str(input())
#    if a.lower() == "komm" :
#        print("Aitäh! oli vaja"+ str(n) + " katse.")
#        break
#    else



###6
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*(10-i))
#print() 
while True:
    try:
        mainnumber = int(input("vali number 1-100:"))
        break
    except ValueError:
        print("see pole täisarv")
if mainnumber<1 or mainnumber>100:
    print("vali õige number")
else:
    paaris = 0
    paaritu = 0
    x = 0
    while x != mainnumber:
        x = x + 1
        print(int(x), end=" ")
        if x % 2 == 0:
            paaris += 1 
        else:
            paaritu += 1




#            print("paaris numbrid"), paaris
#            print("paaritu numbrid") paaritu
