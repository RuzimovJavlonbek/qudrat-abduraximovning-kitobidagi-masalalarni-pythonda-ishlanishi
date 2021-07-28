x1 = float(input("A butun Sonni kiriting:  A =  "))
y1 = float(input("B butun Sonni kiriting:  B =  "))
x2 = float(input("C butun Sonni kiriting:  C =  "))
y2 = float(input("C butun Sonni kiriting:  C =  "))
x3 = float(input("C butun Sonni kiriting:  C =  "))
y3 = float(input("C butun Sonni kiriting:  C =  "))

if x2 == x3 and y2 == y1:
  x4 = x1
  y4 = y3
  print("X4 = " , x4 , "Y4 = " , y4)
elif x2 == x1 and y2 == y3:
  x4 = x3
  y4 = y1
  print("X4 = ", x4, "Y4 = ", y4)

input()