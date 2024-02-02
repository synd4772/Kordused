from random import *


while True:
    try:
        K=int(input("Mitu tk: "))
        if K>0: break
    except ValueError:
        print("Vale tüüp")
while True: 
    try:
        M = int(input("Mitu kotleti ühel pannil?"))
        if M>0: break 
    except ValueError:
        print("Vale tüüp")


#1 {2v}
z = "   (\_/)\n   (o o)\n   / | \*" #Jänesega muutuja
arv = int(input("mitu "))
for i in range(0, 9):
    for j in range(0, arv):
        print(z)
    print()


# 1 {1v}
while True:
    try:
        mitu=int(input("Mitu tk: "))
        if 1 <= mitu < 10:
            break
    except ValueError:
        print("Vale tüüp")

for i in range(mitu):
    print(' /V\ '.center(10, ' '), end="")
print()
for i in range(mitu):
    print(' /\/\ '.center(10,' '), end="")
print()
for i in range(mitu):
    print(' / V V \ '.center(10,' '), end="")
print()
for i in range(mitu):
    print(' /VV V VV\ '.center(10,' '), end="")
print()

  
   
#2
sum = 0
r = int(input("Siseta numbrid"))
for i in range(0, r):
    sum += i

print(sum)

#3
rand = randint(1,100)
print(rand)
for i in range(0, 10):
    vastus = int(input("proovi ära arvata 10 katse arv. "))
    if vastus == rand:
        print("jah!")
        break
    else:
        print("ei!")
        
#4
#v1
arv = str(input("Siseta numbrid "))
summ = ""
for i in reversed(arv):
    summ += i
print(summ)        

#v2
arv = int(input("Siseta numbrid "))
summ = "" #Muutuja, milles hoitakse pöördnumbrit

while arv > 0:
    digit = arv % 10
    arv = arv // 10
    summ += str(digit)

print(summ)
#v3


#5
arv = str(input("Sisetsa numbrid"))
summ = 0
urutamine = 1
for i in arv:
    summ += int(i)
    urutamine *= int(i)

print(summ, urutamine)


# veel:

#5 {5v}
sum_num = 0
sum_km = 0
for i in range(12):
    num = randint(1000,100000)
    km = randint(1,1000)
    sum_num += num  
    sum_km += km
    print(f"{i+1}. maakond. \nElanikud: {num}. Pindala: {km}\nKokku: {sum_num}, {sum_km}\n")
vastus = sum_num / sum_km
print(f"Keskimne: {vastus:.3f}")
 
# ? {?v}
N = 25
kesk1 = 0
kesk2 = 0
for i in range(N):
    h1 = randint(1,5)
    h2 = randint(1,5)
    kesk1 += h1
    kesk2 += h2
kesk1 /= N 
kesk2 /= N

print(f"Keskmine hinne 1 klassis on {kesk1}")
print(f"Keskmine hinne 2 klassis on {kesk2}")