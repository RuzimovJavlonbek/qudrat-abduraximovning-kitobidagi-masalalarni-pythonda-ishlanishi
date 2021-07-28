#Masala sharti . For_10
from math import*
print("For_10.\n\n n butun son berilgan (n>0). \n Quyidagi yig'indini hisoblovchi dastur tuzilsin.\n S= 1+(1/2)+(1/3)+...(1/n)")
# Masala asosiy ko'di
n = int(input(" n sonni kiritng: n = "))

while n <= 0:
  print(" \n Xatolik yuz berdi.  a<b qilib kiriting!!!")
  n = int(input(" n sonni kiritng: n = "))

summa = 0
little = " "
little_2 = " "
for son in range(1,n+1):
  summa += 1/son
  k = 1/son
  satr_2 = str(k)
  little_2 += satr_2 + "  +  "

  if son <= n-1:
   satr = str(son)
   little += "(1/"+satr +")" + " + "
  elif son == n:
   satr = str(son)
   little += "(1/"+satr + ")" + " + "

print(" \n", little, "=", summa , " \n \n ikkinchi usul \n\n")
print(little_2 , " = " , summa)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
