a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))

if (a > b and b>c ) or ( b>a and a>c):
  print("BU uchta sondan eng kichigi:  C = ",c )
elif (a > c and c > b) or (c > a and a > b):
  print("BU uchta sondan eng kichigi:  B = ", b)
elif (b > c and c > a) or (c > b and b > a):
  print("BU uchta sondan eng kichigi:  A = ", a)

input()
