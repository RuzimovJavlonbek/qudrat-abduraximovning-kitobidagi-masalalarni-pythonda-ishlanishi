a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))

if c>b and b>a:
  print(" Sonlar o'sish tartibida kiritildi: ", "\n2 * A = " , 2*a, "\n2 * B = ", 2*b, "\n2 * C = ", 2*c)
else:
  print(" Sonlar o'sish tartibida kiritilmadi : ", "\n -A = ",-a, "\n-B = ", -b, "\n-C = ", -c)

input()