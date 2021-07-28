print(" a va b butun sonlari berilgan (a<b). \n a va b sonlari orasidagi barcha butun sonlarni (a va b dan tashqari )\n kamayish tartibida chiqaruvchi  va chiqarilgan sonlar sonini pragrmma tuzilsin \n\n")

a = int(input(" a ni kiriting:  a ="))
b = int(input(" a ni kiriting:  b ="))
k = 0

for son in range(a+1, b):
  k+=1
  print(k,")  ", son)

input()
