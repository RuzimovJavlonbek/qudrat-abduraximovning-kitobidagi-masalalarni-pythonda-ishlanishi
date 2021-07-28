from math import*
n = float(input("N Butun sonni kiriting:  N= "))
while ceil(n) > n or n <= 0:
  n = float(input("\nXATOLIK YUZ BERDI!!! \nN ga qayta butun son kiriting: N = "))

print("\nKatta raxmat N ni  to'g'ri kiritidingiz.\n")

n = int(n)
summa = 0
for i in range(1, n+1):
  summa += i**n
  print(i, ")  ", i, " ning ", n, " - darajasi ",i**n, " \n      Yig'indi: ", summa, " \n")
  n -= 1

print("Natija: = ", summa)

print(" \n\n  by: Ruzmov_Javlonbek   ")


input()
