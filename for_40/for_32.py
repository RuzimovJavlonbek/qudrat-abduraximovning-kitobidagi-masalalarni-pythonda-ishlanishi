from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n) > n or n < 0:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

n = int(n)
c = 1

print("A 0 = ", c)

for i in range(1, n+1):
  c = (c+1)/i
  print("A", i, " = ", c)

print(" \n\n\n  by: Ruzmov_Javlonbek   ")

input()
