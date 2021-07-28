from math import*
n = float(input("N Butun sonni kiriting:  N= "))
while ceil(n)>n:
  n = float(input("\nXATOLIK YUZ BERDI!!! \nN ga qayta butun son kiriting: N = "))

k = float(input("\nKatta raxmat N  ni  to'g'ri kiritdingiz\n\n Endi esa K Butun sonni kiriting:  K= "))
while ceil(k)>k:
  k = float(input(" \n XATOLIK YUZ BERDI!!! \nK ga qayta butun son kiriting: K = "))

print("\n\nKatta raxmat N ni ham K ni ham to'g'ri kiritidingiz. \n\n")

n = int(n)
k = int(k)

summa = 0
for i in range(1,n+1):
  summa += i**k
  print(i,")  " , i , " ning ", k , " - darajasi ", i**k, " \n      Yig'indi: ", summa, " \n" )

print("Natija: = ",summa)

print(" \n\n\n  by: Ruzmov_Javlonbek   ")

input()
