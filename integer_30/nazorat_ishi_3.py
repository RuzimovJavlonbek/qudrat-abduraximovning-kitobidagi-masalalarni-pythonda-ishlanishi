a = int(input(" 7 xonsli son kiriting: N =  "))


k1 = a%10
k2 = (a%100)//10
k3 = (a%1000)//100
k4 = (a%10000)//1000
k5 = (a%100000)//10000
k6 = (a%1000000)//100000
k7 = a//1000000

if k1==k2 and k2==k3 and k3==k4 and k4==k5 and k5==k6 and k6==k7:
  print(" Bu nomerni narxi 3000$. ")
if k1==k2 and k2==k3 and k3==k4 and k4!=k5 and k1==k6 and k6==k7:
  print("Bu nomerni narxi 2500$")
if k1==k2 and k2==k3 and k3==k4 and k4==k5 and k5==k6 and k6!=k7:
  print(" Bu nomerni narxi 2500$. ")

input()















#if b==7 and a[0]==a[1] and a[0]==a[2] and a[0]==a[3] and a[0]==a[4] and a[0]==a[5] and a[0]==a[6]:
#  print(" Bu nomerni narxi 3000$. ")
#if a[0] == a[1] and a[0]!= a[2] and a[0] == a[3] and a[0] == a[4] and a[0] == a[5] and a[0] == a[6]:
#  print("Bu nomerni narxi 2500$")
#if b!=7 :
#  print(" Siz 7 xonali son kiritmadingiz.")
#else:
#  print(" Bizda bunday raqam yo'q.")
