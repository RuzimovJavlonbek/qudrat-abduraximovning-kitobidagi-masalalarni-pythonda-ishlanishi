#Masala sharti . For_13
from math import*
print("For_13.\n\n n butun son berilgan (n>0). \n Quyidagi yig'indini  hisoblovchi dastur tuzilsin.\n S= 1.1-1.2+1.3-1.4+1.5-...   (n ta qo'shiluvchi, ishoralar almashib keladi.)")

# Masala asosiy ko'di
n = int(input(" n sonni kiritng: n = "))
while n <= 0:
  print(" \n Xatolik yuz berdi.  a<b qilib kiriting!!!")
  n = int(input(" n sonni kiritng: n = "))

summa = 0
little = "  "
#============================Bular oddiy usuli uchun zarur =======================================
summa_2 = 0
ishora = 1
x = 1.1

for son in range(1, n+1):
#============================Bu oddiy usuli  ==========================================
  summa_2 +=ishora*x
  x =round(x+0.1 , 1)
  ishora *= -1
#==========================Bu murakkab usuli ==================================
  k = (10+son) / (10)
  if son%2 ==0 and son < n:
    k = k*(-1)
    satr = str(k)
    little+="("+ satr +" )"+ " + "

  elif son % 2 != 0 and son < n:
    k=k
    satr = str(k)
    little += "(" + satr + " )" + " + "

  elif son % 2 == 0 and son == n:
    k = k*(-1)
    satr = str(k)
    little += "(" + satr + " )"

  elif son % 2 != 0 and son == n:
    k = k
    satr = str(k)
    little += "(" + satr + " )"
  summa = round(summa + k, 1)

print(little,  " = " , summa)
print("NATIJAAAA Oddiy usulda:  " , round(summa_2,1))
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
