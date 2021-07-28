#Masala sharti . For_12
from math import*
print("For_12.\n\n n butun son berilgan (n>0). \n Quyidagi ko'paytmani  hisoblovchi dastur tuzilsin.\n S= 1.1*1.2*1.3*...   (n ta ko'paytuvchi)")

# Masala asosiy ko'di
n = int(input(" n sonni kiritng: n = "))

while n <= 0:
  print(" \n Xatolik yuz berdi.  a<b qilib kiriting!!!")
  n = int(input(" n sonni kiritng: n = "))

summa = 1
k = 1
little = " "
for son in range(1,n+1):
  k = round(k+0.1,1)
  summa *= k

  if son <= n-1:
   satr = str(k)
   little += satr + " * "
  elif son == n:
   satr = str(k)
   little += satr
print(" \n", little, "=", summa)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
