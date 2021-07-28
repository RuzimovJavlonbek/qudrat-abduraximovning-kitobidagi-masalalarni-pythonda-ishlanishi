#Masala sharti . For_7
from math import*
print("For_7.\n\n a va b butun sonlar berilgan (a<b). \n a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaruvchi pragramma tuzilsin. \nBu yerda  a  ni ham b ni  ham  oladi. ")

# Masala asosiy ko'di
a = int(input(" a sonni kiritng: a = "))
b = int(input(" b sonni kiritng: b = "))

massiv = []

summa = 0
little = " "


while a>b:
  print(" a<b  qilib kiritmadingiz. Iltimos qayta kiriting. ")
  a = int(input(" a sonni kiritng: a = "))
  b = int(input(" b sonni kiritng: b = "))


for son in range(a, b+1):
  summa +=son
  if son <= b-1:
    satr = str(son) + "+"
    little += satr
    massiv.append(son)
  elif son == b:
    satr = str(son)
    little += satr
    massiv.append(son)

print("BU massiv: =",  massiv , "  = " , sum(massiv))
print(little, "=" ,summa)
print(" \n\n\nby: Ruzimov_Javlonbek")

input()
