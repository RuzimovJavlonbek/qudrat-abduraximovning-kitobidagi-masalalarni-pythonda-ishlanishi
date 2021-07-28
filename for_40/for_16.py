from math import*
print(" For_16 \n\n")


n = float(input(" n Butun son kiritng: N = "))
while n < 0 or ceil(n) > n:
  print(" \n\nXATOLIK YUZ BERDI!!! \n   Iltimos N ga butun son kiriting.  ")
  n = float(input(" Iltimos qaytadan  N butun son kiritng: N = "))

print(" N  ni  to'g'ri  kiritganingiz uchun katta raxmat. ! \n")

a = float(input(" Endi esa  b  haqiqiy sonni kiriritng:  a ="))

n = int(n)
kupaytma = 1
summa = 0
for son in range(n+1):

  k = a**son
  summa += k

  print(son, ")  ", a, "  ning  ", son,"  - darajasi  ",   k, "  ga  teng. ")
print(" \n\nDarajalar  yig'indisi:   " , summa)

input()
