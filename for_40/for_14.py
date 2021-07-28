#Masala sharti . For_14
from math import*
print("For_14.\n\n n butun son berilgan (n>0). \n Shu sonni kvadratini  quyidagi fo'rmula asosida hisoblovchi dastur tuzilsin.\n n*n= 1+3+5+7+ ...+(2*n-1) ")

# Masala asosiy ko'di
n = int(input(" n sonni kiritng: n = "))

while n <= 0:
  print(" \n Xatolik yuz berdi.  a<b qilib kiriting!!!")
  n = int(input(" n sonni kiritng: n = "))

summa = 0
little = " "
for son in range(1, n+1):
  summa += (2*son-1)

  if son <= n-1:
   satr = str(2*son-1)
   little += satr + " + "
  elif son == n:
   satr = str(2*son-1)
   little += satr

print("Natija: ",n," ning kvadrati  = ", little," = ", summa)

print(" \n\n\nby: Ruzimov_Javlonbek")
input()
