#Masala sharti . For_6
from math import*
print("For_6.\n\n1 kg konfet narxi berilgan ( haqiqiy son ). \n  1.2, 1.4, 1.6 ,...  2 kg konfet narxini chiqaruvchi pragramma tuzing. ")

# Masala asosiy ko'di
narx = float(input("\n\n 1 kg konfet narxini kiriting: narx =  "))

k = 1.2
for sanoq in range(1, 6):
    kg_narx = k*narx
    print("{} )  {} kg  konfet narxi,  {} * {}  =  {}   ga teng ekan ".format(sanoq,
          k, k, narx, kg_narx))
    k = round(k+0.2, 1)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
