a = int(input( " 4 xonali sonni kiriting: N = "))

k1 = a%10
k2 = (a%100)//10
k3 = (a%1000)//100
k4 = a//1000

if k1==k4 and k2==k3:
  print("Barakalla  siz kiritgan son PALINDROM SON.")
else :
  print(" Uzr bu POLINDROM  son emas.")

input()
























#b = len(a)

#if b==4:
#  print("Raxmat siz kiritgan son 4 xonali son ekan.")
#else:
#  print(" Uzr siz 4 xonali kiritmadingiz.")
