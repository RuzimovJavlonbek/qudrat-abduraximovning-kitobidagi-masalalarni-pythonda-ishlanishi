a = int(input("Uch hinali sonni kriting: N="))
k1 = a%10
k2 = (a%100)//10
k3 = a//100

if  k3>k2 and k3>k1 and k2>k1:
  print("Siz kiritgan sonni raqamlari kamayish tartibida yozilgan.")
else :
  print("Siz kiritgan sonni raqamlari kamayish tartibida yozilmagan.")

input()