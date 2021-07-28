n = int(input("Yilni kiriting: "))

if  n%100 > 0 and n%4 == 0:
  print(" BU Yil Kabisa yili ekan: Demak 366 kun bor.  ")
elif n%100 == 0 and n%400 == 0:
  print(" BU Yil Kabisa yili ekan: Demak 366 kun bor!  ")

else:
  print(" BU Yil Kabisa yili emas: Demak 365 kun bor.  ")

input()
