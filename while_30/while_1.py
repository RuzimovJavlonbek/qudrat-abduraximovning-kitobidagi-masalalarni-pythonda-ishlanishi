from math import*
a = float(input(" A  butun musbat sonni kiriting: A = "))

while ceil(a) > a  or a<=0:
  a = float(input(" \n XATOLIK YUZ BERDI! \n  A ni  butun musbat son qilib  qayta  kiriting: A = "))

b = float(input(" \n Katta raxmat A ni to'g'ri kiritdingiz! \n Endi   B  butun musbat sonni B < A qilib  kiriting: B = "))

while ceil(b) > b or b <= 0 or b > a :
  b = float(input(" \n XATOLIK YUZ BERDI! \n  B butun musbat sonni B < A qilib  qayta  kiriting: B = "))

print(" \n Katta raxmat B  ni  ham to'g'ri kiritdingiz! ")

a =int(a)
b =int(b)
c=a
k = 0
while a>b:
  a-=b
  k+=1

print("\n Natija: ", c, " ni ichida  " , b ," , ", k , " marta joylashadi.  \nOrtib qolgan qismi esa :  ", a , " ga teng")

print("\n\n\n   by:  Ruzimov  Javlonbek ")
input()
