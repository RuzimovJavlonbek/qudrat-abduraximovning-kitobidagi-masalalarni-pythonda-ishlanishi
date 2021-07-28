
'''
Array_1
n = int(input(" N sonni kiriting: N= "))

massiv_toq_son = []

for i in range(n):
  massiv_toq_son.append(2*i+1)
  print(massiv_toq_son)
input()
'''

#===========================================================================================
'''
Array_1
n = int(input(" N sonni kiriting: N= "))

massiv_ikkini_darajasi = []

for i in range(n+1):
  massiv_ikkini_darajasi.append(2**i)
print(massiv_ikkini_darajasi)
input()
'''
#===============================================================================================
'''
#Array_3

n = int(input(" N sonni kiriting: N= "))
a = int(input(" A Pragressiya dastlabki hadi: A= "))
d = int(input(" D Pragressiya  ayirmasi: D= "))

massiv_pragressiya = [a]

for i in range(n+1):
  massiv_pragressiya.append(massiv_pragressiya[i-1] + d)

print(massiv_pragressiya)
input()
'''
'''
a = int(input())
satr = str(a)
print(" 1/" +satr)
'''
from cmath import*
print(factorial(0) )


input()