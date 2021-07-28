from math import*
print(" For_15 \n\n")


n = float(input(" n Butun son kiritng: N = "))
while n<0 or ceil(n)>n:
  print(" \n\nXATOLIK YUZ BERDI!!! \n   Iltimos N ga butun son kiriting.  ")
  n = float(input( " Iltimos qaytadan  N butun son kiritng: N = "))

print(" N  ni  to'g'ri  kiritganingiz uchun katta raxmat. ! \n")

a = float(input(" Endi esa  b  haqiqiy sonni kiriritng:  a ="))

kupaytma = 1
n = int(n)

for son in range(1, n+1):

  kupaytma *=a
  print(son , ")  " , a , "  ning  " , son , "  - darajasi  ",   kupaytma , "  ga  teng. ")

input()
