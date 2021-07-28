#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  23.06.2021
# Maniz: Nukus

# Begin .

print("Begin_21.  \n     ")

from math import *

x1 = float(input(" X1  ni kiriting:  "))
y1 = float(input(" Y1  ni kiriting:  "))
x2 = float(input(" X2  ni kiriting:  "))
y2 = float(input(" Y2  ni kiriting:  "))
x3 = float(input(" X3  ni kiriting:  "))
y3 = float(input(" Y3  ni kiriting:  "))

a = sqrt((x2-x1)**2 + (y2-y1)**2 )
b = sqrt((x3-x1)**2 + (y3-y1)**2 )
c = sqrt((x3-x2)**2 + (y3-y2)**2 )

p = a+b+c

p_yarim = p/2

s = sqrt(p_yarim*(p_yarim-a)*(p_yarim-b)*(p_yarim-c))

print("Peremetr: ", p , " \nYuzasi: ", s )


input()
