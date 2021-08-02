from math import*
n = float(input(" N > 0.  Butun son kiriting: "))
while ceil(n) > n or n < 0:
  n = float(input("\n\n XAROLIK YUZ BERDI!!! \n  N ni qayta kiriting.  N > 0  Butun son kiriting: "))
n = int(n)
k = 1
while n>=2:
  k*=n
  n-=2

print("\n Natija: = ",k)

print("\n\n by:  RUZIMOV_Javlonbek")

input()
