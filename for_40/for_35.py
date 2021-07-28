from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n) > n or n <= 1:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

n = int(n)
a = 1
b = 2
c = 3

print("F 1 = 1")
print("F 2 = 2")
print("F 3 = 3")

for i in range(4, n+3):
  d = c + b-2*a
  a = b
  b = c
  c = d
  print("F", i, " = ", d)

print(" \n\n\n  by: Ruzmov_Javlonbek   ")


input()
