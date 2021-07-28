#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_12.  \n     ")


a = input(" Uch honali son:   A=")

#=============================================1-usul===========================================================
print("Natija: ", a[::-1])

#=============================================2-usul===========================================================

a = int(a)
print("Natija: ", ((a%100)//10)*10 + (a % 10)*100 + a//100)

input()
