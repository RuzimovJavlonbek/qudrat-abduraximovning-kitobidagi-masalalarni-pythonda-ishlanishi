#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  24.06.2021
# Maniz: Nukus

# Begin .

from math import *
print("Begin_40.  \n     ")


a1 = float(input("A ni kiriting: A1 = "))
b1 = float(input("B ni kiriting: B1 = "))
c1 = float(input("C ni kiriting: C1 = "))
a2 = float(input("A ni kiriting: A2 = "))
b2 = float(input("B ni kiriting: B2 = "))
c2 = float(input("C ni kiriting: C2 = "))


d = (a1*b2 - a2*b1)

x = (c1*b2-c2*b1)/d
y = (a1*c2-a2*c1)/d


print(" X= ", x, " Y = ", y)


input()
