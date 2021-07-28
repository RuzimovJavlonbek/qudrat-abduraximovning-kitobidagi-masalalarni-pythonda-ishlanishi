a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))


if (a > b and b>c ) or ( b>a and a>c):
  print("BU uchta sondan yig'indisi eng katta bo'ladigan ikkita son:  A = ", a, "   B = ", b, "\nA + B = ", a+b)
elif (a > c and c > b) or (c > a and a > b):
  print("BU uchta sondan yig'indisi eng katta bo'ladigan ikkita son:  A = ",a, "    C = ", c, "\nA + C = ", c+a)
elif (b > c and c > a) or (c > b and b > a):
  print("BU uchta sondan yig'indisi eng katta bo'ladigan ikkita son:  C = ", c, "   B = ", b , "\nC + B = " , c+b)


input()
