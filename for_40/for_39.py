from math import*
a = float(input("A  Butun sonni  kiriting:  A ="))
while ceil(a) > a:
  a = float(input("\n XATOLIK YUZ BERDI!!! \n A ga qayta Butun sonni  kiriting:  A ="))

b = float(input("\nRaxmat A ni to'g'ri kiritidingiz\n\n Endi  B ni  Butun  son  A<B qilib kiriting:  B = "))
while ceil(b) > b or a > b:
  b = float(input("\n XATOLIK YUZ BERDI!!! \n B ni  Butun  son  A<B  qilib  kiriting:  B = "))

a = int(a)
b = int(b)
if a==b:
  print(0)

while a <= b:
  if a>=0:
    k = a
    if a == 0:
      k=1
    satr = str(a) + "  "
    print(satr*k)
    a += 1

  elif a<0:
    k = -a
    satr = str(a) + "  "
    print(satr*k)
    a += 1

print(" \n\n  by: Ruzmov_Javlonbek   ")
input()
