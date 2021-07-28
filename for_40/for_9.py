#Masala sharti . For_9
from math import*
print("For_9.\n\n a va b butun sonlar berilgan (a<b). \n a dan b gacha bo'lgan barcha butun sonlar kvadratlarining  yig'indisini  chiqaruvchi pragramma tuzilsin. \nBu yerda  a  ni ham b ni  ham  oladi. ")

# Masala asosiy ko'di
a = int(input(" a sonni kiritng: a = "))
b = int(input(" b sonni kiritng: b = "))

while a>b:
  print(" Xatolik yuz berdi.  a<b qilib kiriting!!!\n\n  ")
  a = int(input(" a sonni kiritng: a = "))
  b = int(input(" b sonni kiritng: b = "))

summa = 0
little = " "
for son in range(a, b+1):
  summa += son**2
  if son <= b-1:
   satr = str(son**2) + " + "
   little += satr
  elif son == b:
    satr = str(son**2)
    little += satr


print(" \n", little, "=", summa)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
