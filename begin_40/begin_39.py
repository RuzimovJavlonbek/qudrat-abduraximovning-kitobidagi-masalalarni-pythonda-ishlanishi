#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Begin .

from math import *
print("Begin_39.  \n     ")


a = float(input("A ni kiriting: A = "))
b = float(input("B ni kiriting: B = "))
c = float(input("C ni kiriting: C = "))

d = b**2 - 4*a*c

x1 = (-b-sqrt( d))/(2*a)
x2 = (-b+sqrt( d))/(2*a)


print(" X1= ", x1 , " X2 = " , x2)


input()
