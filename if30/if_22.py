a = float(input("A butun Sonni kiriting:  X =  "))
b = float(input("B butun Sonni kiriting:  Y =  "))

if a > 0 and b > 0:
  print(" I-Chorak")
elif b > 0 and a < 0:
  print(" II-chorak")
elif a < 0 and b < 0:
  print("III-chorak")
elif a > 0 and b < 0:
  print("IV-Chorak")

else:
  print("Itimos qayta kiriting.")

input()
