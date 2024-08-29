#Botirov Davron
import os
os.system('cls')
os.system('color 2')
sonlar = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
]
rimraqam = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
]
son = int(input("3999 dan oshmidigan son kiriting: "))
if 1 <= son <= 3999:
    natija = ''
    i = 0
    while son > 0:
        for _ in range(son // sonlar[i]):
            natija += rimraqam[i]
            son -= sonlar[i]
        i += 1
    print(f" rim raqamida: {natija}")