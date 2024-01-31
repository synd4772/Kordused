from random import *

#1
z = "   (\_/)\n   (o o)\n   / | \*"
arv = int(input("mitu "))
for i in range(0, 9):
    for j in range(0, arv):
        print(z)
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
arv1 = 0
summ = ""

while arv > 0:
    digit = arv % 10
    arv = arv // 10
    summ += str(digit)

print(summ)

#5
arv = str(input("Sisetsa numbrid"))
summ = 0
urutamine = 1
for i in arv:
    summ += int(i)
    urutamine *= int(i)

print(summ, urutamine)