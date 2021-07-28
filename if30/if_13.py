a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))


if (a > b and b > c) or (c > b and b > a):
  print("BU uchta sondan o'rtachasi:  B = ", b)

elif (a > c and c > b) or (b > c and c > a):
  print("BU uchta sondan o'rtachasi:  C = ", c)

elif (b > a and a > c) or (c > a and a > b):
  print("BU uchta sondan o'rtachasi:  A = ", a)

input()
