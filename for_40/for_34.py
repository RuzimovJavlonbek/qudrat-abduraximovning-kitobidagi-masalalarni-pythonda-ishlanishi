
from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n) > n or n <= 1:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

n = int(n)
a = 1
b = 2

print("F 1 = 1")
print("F 2 = 2")

for i in range(3, n+3):
  c = (a+2*b)/3
  a = b
  b = c
  print("F", i, " = ", c)

print(" \n\n\n  by: Ruzmov_Javlonbek   ")

input()
