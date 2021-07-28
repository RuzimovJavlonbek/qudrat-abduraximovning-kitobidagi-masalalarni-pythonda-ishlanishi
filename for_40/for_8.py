#Masala sharti . For_8
from math import*
print("For_8.\n\n a va b butun sonlar berilgan (a<b). \n a dan b gacha bo'lgan barcha butun sonlar ko'paytmasini  chiqaruvchi pragramma tuzilsin. Bu yerda  a  ni ham b ni  ham  oladi. ")

# Masala asosiy ko'di
a = int(input(" a sonni kiritng: a = "))
b = int(input(" b sonni kiritng: b = "))

while a > b:
  print(" a<b  qilib kiritmadingiz. Iltimos qayta kiriting. ")
  a = int(input(" a sonni kiritng: a = "))
  b = int(input(" b sonni kiritng: b = "))



summa = 1
little = " "
for son in range(a, b+1):
  summa *= son
  if son <= b-1:
   satr = str(son) + " * "
   little += satr
  elif son == b:
    satr = str(son)
    little += satr
    print(" \nBumi factorial funksiaysi orqali chiqardim.!!!   Natija: ", factorial(son))

print(" \n", little, "=", summa)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
