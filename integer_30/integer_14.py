#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Integer.

from math import *
print("Integer_14.  \n     ")


a = int(input(" Uch honali son:   A="))

#=============================================2-usul===========================================================

print("Natija: ", (a % 100)//10 + (a % 10)*100 + (a//100)*10 )

input()
