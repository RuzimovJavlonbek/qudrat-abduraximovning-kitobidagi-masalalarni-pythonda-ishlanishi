from math import*
a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))

if fabs(a-b) > fabs(a-c):
  print(" A nuqtaga  C nuqta yaqin ekan: C = " , c , "  \n Kesma uzunligi: = ",fabs(a-c))

elif fabs(a-b) < fabs(a-c):
  print(" A nuqtaga  B nuqta yaqin ekan: B = ",b, "  \n Kesma uzunligi: = ", fabs(a-b))

else:
  print(" Ikkita nuqta ham bir hil uzoqllikda ekan.")
  
input()
