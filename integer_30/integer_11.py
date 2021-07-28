#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_11.  \n     ")

a= input(" uch honali son:    A=")

#=============================================1-usul===========================================================
print("Natija : ", int(a[2]) + int(a[1]) + int(a[0]))

#=============================================2-usul===========================================================

a = int(a)
print("Natija2: ", a%10 + (a%100)//10 + a//100 )

input()
