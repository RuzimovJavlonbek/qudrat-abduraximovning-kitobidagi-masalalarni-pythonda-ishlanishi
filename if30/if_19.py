a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))
d = float(input("D butun Sonni kiriting:  D =  "))

if a == b == c:
  print(" D teng emas:  4")
elif a == c == d:
   print(" B teng emas:  2")
elif b == c == d:
   print(" A teng emas:  1")
elif a == b == d:
   print(" C teng emas:  3")

else:
  print("Siz kiritgan son qonunyatga tug'ri kelmaydi. ")

input()
