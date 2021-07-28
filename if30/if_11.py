a = int(input("A butun Sonni kiriting:  A =  "))
b = int(input("B butun Sonni kiriting:  B =  "))

if a != b and a>b:
  b = a
  print("A = ", a, "B = ",  b)

elif a != b and a < b:
  a = b
  print("A = ", a, "B = ",  b)

elif a == b:
  a = 0
  b = 0
  print("A = ", a, "B = ",  b)

input()


