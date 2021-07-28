#Bu dastur Qudrat Abduraximovning C++ ga asoslangan  kitobidagi masalar asosida python dasturlash tilida yozildi
# O'rganuvchi bo'lajak  dasturchi :  J_Ruzimov
#Sana:  21.06.2021
# Maniz: Nukus

# Begin 6

print("Begin_6.  \n  Paralelipedning  tomonlari  a, b, c, berilgan. Uning hajmi  V = a*b*c va to'la sirti \n S = 2*(a*b + b*c + a*c)   aniqlansin . ")

paraleliped_tomon1 = int(input(" Paralelipedning   1-tomonini  kiriting:  A= "))
paraleliped_tomon2 = int(input(" Paralelipedning   2-tomonini  kiriting:  B= "))
paraleliped_tomon3 = int(input(" Paralelipedning   3-tomonini  kiriting:  C= "))

v = paraleliped_tomon1*paraleliped_tomon2*paraleliped_tomon3
s = 2*(paraleliped_tomon1*paraleliped_tomon2 + paraleliped_tomon2*paraleliped_tomon3 + paraleliped_tomon1*paraleliped_tomon3 )


print(" Tomonlari , " , paraleliped_tomon1 , "  , "  , paraleliped_tomon2 , "  , " , paraleliped_tomon3 , "  bo'lgan paralelipedning , \n  Hajmi V = " , v , " \n To'la sirti esa  S = ", s , "  ga teng. ")


input()
