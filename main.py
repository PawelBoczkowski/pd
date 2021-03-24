import random


haslo = ""
with open("slowa.txt","r") as file:
    lines = file.read().splitlines()
haslo = random.choice(lines)
literki_hasla = []

#11

podpowiedz = 0

for el in haslo:
    literki_hasla.append(el)

gra = True
wisielec = 0
print("1.Rozpocznij gre")
print("2.Wyjdz z gry")
menu = input("Wybor:")
while gra or wisielec == 11:
    if menu == '1':
        wybor = input("podaj literke:")
        for el in literki_hasla:
            if wybor == el in literki_hasla:
                print("zgadles literke", el)
                literki_hasla.remove(el)
                print(literki_hasla)
                if not literki_hasla:
                    print("gratulacje odgadles haslo")
                    gra = False
            else:
                print("nie zgadles")
                podpowiedz += 1
                if podpowiedz == 3:
                    porada = input("potrzebujesz podpowiedzi? T- tak N- nie:")
                    if porada == "T":
                        print(f"haslo ma {len(haslo)} liter")
                    else:
                        podpowiedz = 0
                        break
                break
    if menu == '2':
        gra = False





