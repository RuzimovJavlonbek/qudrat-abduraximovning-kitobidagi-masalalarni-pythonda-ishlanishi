from math import*
print(" For_ 20\n\n")
n = float(input(" _N_  Nechagacha bo'lgan sonlarning factoriali yig'indisi kerak:  "))

while ceil(n) > n or n <= 0:
  n = float(input(" XATOLIK!!!\n Iltimos n>0 qilib  qayta kiriritng: n = "))

suma1 = 0

n = int(n)

for i in range(1,n+1):
  c = factorial(i)
  print(i," )   " , i ,"! = ", c )
  suma1 += c
print(" Hammasini yig'indisi: Summa = " , suma1)

input()
