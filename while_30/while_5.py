from math import*
n = float(input("N butun son kiriting. N>0 : N = "))
while ceil(n) > n or n < 0:
  n = float(input(" \n XATOLIK YUZ BERDI!!! \n Qayata kiting. N butun son kiriting. N>0 : N = "))
n = int(n)

k = 1
while 2**k < n:
  k += 1
  if 2**k == n:
    print("\n",n, " soni  2 ning ",  k, " -  darajasi ekan.")

if 2**k > n:
  print("\n ",n, " soni  2 ning   darajasi emas.")

input()
