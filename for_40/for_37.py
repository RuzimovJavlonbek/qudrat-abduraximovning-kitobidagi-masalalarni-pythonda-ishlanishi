from math import*
n = float(input("N Butun sonni kiriting:  N= "))
while ceil(n) > n:
  n = float(input("\nXATOLIK YUZ BERDI!!! \nN ga qayta butun son kiriting: N = "))

print("\nKatta raxmat N ni  to'g'ri kiritidingiz.\n")

n = int(n)

summa = 0
for i in range(1, n+1):
  summa += i**i
  print(i, ")  ", i, " ning ", i, " - darajasi ",i**i, " \n      Yig'indi: ", summa, " \n")

print("Natija: = ", summa)

print(" \n\n\n  by: Ruzmov_Javlonbek   ")

input()
