#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_10.  \n     ")

a = input(" uch honali son:    A=")

#=============================================1-usul===========================================================
print("Birlik : ", a[2] , "\n O'nlik: " , a[1] )


#=============================================2-usul===========================================================

a = int(a)
print("Birlik : ", a%10, "\n O'nlik: ", (a%100)//10 )

input()
