#Masala sharti . For_5
from math import*
print("For_5.\n\n1 kg konfet narxi berilgan ( haqiqiy son ). \n  0.1, 0.2, 0.3 ,...1 kg konfet narxini chiqaruvchi pragramma tuzing. ")

# Masala asosiy ko'di
narx = float(input("\n\n 1 kg konfet narxini kiriting: narx =  "))

k = 0.1
for sanoq in range(1, 11):
    kg_narx = k*narx
    print("{} )  {} kg  konfet narxi,  {} * {}  =  {}   ga teng ekan ".format(sanoq,k, k, narx, kg_narx))
    k = round(k+0.1, 1)
print(" \n\n\nby: Ruzimov_Javlonbek")
input()
