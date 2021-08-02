from math import*
n = float(input("N butun son kiriting. N>0 : N = "))
while ceil(n)>n or n < 0:
  n = float(input("\nXATOLIK YUZ BERDI!!!\n Qayata kiting. N butun son kiriting. N>0 : N = "))
n = int(n)

k = 1
while 3**k < n:
  k+=1
  if 3**k == n:
    print("\n", n  , " soni  3 ning ",  k   ," -  darajasi ekan.")

if 3**k > n:
  print("\n", n, " soni  3 ning   darajasi emas.")

input()
