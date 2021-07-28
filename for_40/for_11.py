#Masala sharti . For_11
from math import*
print("For_11.\n\n n butun son berilgan (n>0). \n Quyidagi yig'indini hisoblovchi dastur tuzilsin.\n S= n*n + (n+1)*(n+1) + (n+2)*(n+2) + ...(2*n)*(2*n) ")

# Masala asosiy ko'di
n = int(input(" n sonni kiritng: n = "))

while n <= 0:
  print(" \n Xatolik yuz berdi.  a<b qilib kiriting!!!")
  n = int(input(" n sonni kiritng: n = "))

summa = 0
little = " "

for son in range(n+1):
  summa += (n+son)**2

  if son <= n-1:
   k = (n+son)**2
   satr = str(k)
   little += satr  + " + "
  elif son == n:
   k = (n+son)**2
   satr = str(k)
   little += satr

print(" \n", little, "=", summa)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
