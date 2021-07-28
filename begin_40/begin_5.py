#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  21.06.2021
# Maniz: Nukus

# Begin 5

import math

print("Begin_5.  \nKubning  qirrasi  a  berilgan. Uning hajmini  V= a*a*a   va  to'la  sirti  S = 6*a*a  aniqlansin.")

kubni_qirrasi =  int(input(" Kubni  tomonini  kiriting:  a= "))

hajm = kubni_qirrasi**3
tula_sirti = 6*(kubni_qirrasi**2)

print (" Qirrasi  " , kubni_qirrasi , "  ga teng  bo'lgan  kubning \n hajmi  H = ", hajm , "  ga teng, \n to'la sirti esa  S = " , tula_sirti  , " ga teng  ")


input()
