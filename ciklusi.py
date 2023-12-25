# ciklusi za poctoruvanje so broenje
# ciklusi za povtoruvanje so uslov


#for brojac in range(9):          # [0,1,2,3....n-1]
    #print("Hello World")

#for brojac in range(5):
    #print(brojac)

# korisnikot da vnese 5 broevi i tie broevi da se soberat megju sebe
"""
zbir = 0
br = int(input("Kolku sakate da se povtori"))
for i in range(br):
    broj = int(input("Vnesete broj: "))
    zbir = zbir + broj

print(f"Zbirot na broevite koi gi vnesovte e: {zbir}")
"""

"""broj = 0
while broj < 100:
    broj = int(input("Vnesete broj pomal od 100: "))
    print(broj)"""

#korisnikot da moze da vnesuva broevi se dodeka tie se parni
"""broj= 2
while broj % 2 == 0:
    broj = int(input("Vnesete paren broj"))
    print(broj)"""

while True:
    broj = int(input("Vnesete paren broj"))
    print(broj)

    if broj % 2 != 0:
        print("Vnesovte ne paren broj")
        break

print("Ova e nadvor od while") 



