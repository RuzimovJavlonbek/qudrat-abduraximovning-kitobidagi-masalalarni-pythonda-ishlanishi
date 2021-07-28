a = float(input("A butun Sonni kiriting:  A =  "))
b = float(input("B butun Sonni kiriting:  B =  "))
c = float(input("C butun Sonni kiriting:  C =  "))


if (a > b and b > c) or (b > a and a > c):
  if  a>b:

    print("BU uchta son o'sish tartibida:    ", c ,"<", b, "<" , a)

  elif b>a:
    print("BU uchta son o'sish tartibida:    ", c, "<", a, "<", b)

elif (a > c and c > b) or (c > a and a > b):
  if a > c:

    print("BU uchta son o'sish tartibida:    ", b, "<", c, "<", a)

  elif c > a:
    print("BU uchta son o'sish tartibida:    ", b, "<", a, "<", c)


elif (b > c and c > a) or (c > b and b > a):
  if b > c:

    print("BU uchta son o'sish tartibida:    ", a, "<", c, "<", b)

  elif c > b:
    print("BU uchta son o'sish tartibida:    ", a, "<", b, "<", c)



input()
