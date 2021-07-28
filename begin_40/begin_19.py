#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  22.06.2021
# Maniz: Nukus

# Begin .

print("Begin_19.  \n\nBu dastur koordinata tekisligida qarama, qarshi uchlarining  nuqtalri berilgan ,\nva tomonlari koordinata o'qlariga parallel \nbo'lgan to'gri to'rtburchakni yuzini hisoblab beradi.\n    ")

from math import *

x1 = float(input("X1 ni kiriting: "))
y1 = float(input("Y1 ni kiriting: "))
x3 = float(input("X3 ni kiriting: "))
y3 = float(input("Y3 ni kiriting: "))

x2 = x1
y2 = y3

x4 = x3
y4 = y1

a = sqrt( (x2-x1)**2 + (y2-y1)**2 )
b = sqrt( (x4-x1)**2 + (y4-y1)**2 )

s = a*b
p = 2*(a+b)

print("Yuza: ", s, " \n Peremetr: " , p )

input()
