
from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n) > n or n <= 1:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

n = int(n)
a = 1
b=1

#print("F 1 = 1")
#print("F 2 = 1")

letter = " 1  1"

for i in range(3, n+3):
  c=a+b
  letter += "  " + str(c)
  a = b
  b = c


  #print("F", i, " = ", c)
print(" \n ",letter)
print(" \n\n\n  by: Ruzmov_Javlonbek   ")

input()
