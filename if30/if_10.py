a = int(input("A butun Sonni kiriting:  A =  "))
b = int(input("B butun Sonni kiriting:  B =  "))

if a != b:
  c = a+b
  a = c
  b = c
  print("A = ", a , "B = ",  b)

elif a==b:
  a = 0
  b = 0
  print("A = ", a, "B = ",  b)

input()
