#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_8.  \n     ")

a = input("   A=")

#=============================================1-usul===========================================================
print("Natija: ", a[::-1])

#=============================================2-usul===========================================================

a = int(a)
print("Natija: " , a//10 + (a%10)*10 )

input()
