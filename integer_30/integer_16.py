#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_16.  \n     ")

a = int(input(" Uch honali son:   A="))

#=============================================2-usul===========================================================

print("Natija: ", ((a % 100)//10 + (a % 10)*10 + (a//100)*100))

input()
