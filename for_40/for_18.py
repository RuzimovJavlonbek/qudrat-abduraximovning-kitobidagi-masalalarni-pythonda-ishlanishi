print(" FOR_18\n\n")
a = float(input(" Qaysi sonni darajasini  hisoblamoqchisiz? Shu sonni  kiriritng:  a = "))
n = int(input( "\na ning  nechanchi darajasini  hisoblamoqchisiz ? \n  nechanchi darajani hisoblamoqchisiz.\n   N > 0  bo'lgan butun va haqiqiy sonni kiriting:  N = "  ))

if n <= 0:
  print(" \nXatolik yuz berdi.    N >0   qilib kiritmadingiz !!! \n  Iltimos   N ni qayta kiriting. \n")
  n = int(input(" N > 0  bo'lgan butun va haqiqiy sonni kiriting:  N = "))


summa = 1


for son in range(1 , n+1):
  k = ((-1)**son) * (a**son)
  summa += k
  print( son , " )      k = " , k , "  ,  summa =  ", summa )

print(" \n\n\n SUMMA= 1  SUMMA boshlangich holatda  1 ga teng.\n\n  SUMMA =  " , summa )

print( " \n\n\n  by: Ruzmov_Javlonbek   ")

input()