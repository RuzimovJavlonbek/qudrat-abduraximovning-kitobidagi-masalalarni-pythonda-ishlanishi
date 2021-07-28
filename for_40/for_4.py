#Masala sharti . For_4
print( "For_4.\n\n1 kg konfet narxi berilgan ( haqiqiy son ). \n  1, 2, 3 ,...10 kg konfet narxini chiqaruvchi pragramma tuzing. ")

# Msala asosiy ko'di
narx = float(input("\n\n 1 kg konfet narxini kiriting: narx =  "))
k = 0
for vazn in range(1, 11):
  k += 1
  kg_narx = k*narx
  print("{} )  {} kg  konfet narxi,  {} * {}  =  {}   ga teng ekan ".format(k, k, k , narx, kg_narx))


print(" \n\n\nby: Ruzimov_Javlonbek")
input()
