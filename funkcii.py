# Keep your code DRY

# Don't 
# Repeat
# Yourself

def pecati_poraka(ime):
    print(f"Zdravo {ime}, {prezime}")
    print("Hello World \n\n")

def zbir(broj1, broj2=2):
    rezultat = broj1+broj2
    return rezultat
    

x = 53
y = 12

rezultat_od_zbir = zbir(x,y)
rezultat_od_zbir2 = zbir(10, 5)
print(rezultat_od_zbir)
print(rezultat_od_zbir2)