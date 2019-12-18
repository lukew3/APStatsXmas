import random
b = 0.00
l = 0.00
c = 0.00

for x in range(25): #repeat 25 times
    num = random.randint(1,100) #generates random number 1-100
    #Bob has 14% chance, Lilian has 52% chance, Chester has 34% chance of answering
    if (num >= 1 and num <= 14):
        print("Bob")
        b=b+1
    elif (num >= 15 and num <= 66):
        print("Lilian")
        l=l+1
    elif (num >= 67 and num <= 100):
        print("Chester")
        c=c+1

#Calculates and displays probability of each elf getting picked
b = b / 25.00
l = l / 25.00
c = c / 25.00
print(b)
print(l)
print(c)
