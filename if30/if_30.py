#================Whileni O'chirsak bitta aylanishda to'xtaydi=================================
#====================Shu turishda dastur uzluksiz ishlaydi
n = input("  1 < N < 999 Son kiriting: N =  ")
a = len(n)

if n.isdigit() and int(n) > 0 and int(n) <= 999:
  if a == 1 and int(n) % 2 == 0:
    print(" \nSiz kiritgan son bir xonali juft son. ")

  elif a == 1 and int(n) % 2 != 0:
    print(" \nSiz kiritgan son bir xonali toq son. ")
  elif a == 2 and int(n) % 2 == 0:
    print(" \nSiz kiritgan son ikki xonali juft son. ")
  elif a == 2 and int(n) % 2 != 0:
    print(" \nSiz kiritgan son ikki xonali toq son. ")
  elif a == 3 and int(n) % 2 == 0:
    print(" \nSiz kiritgan son uch xonali juft son. ")
  elif a == 3 and int(n) % 2 != 0:
      print(" \nSiz kiritgan son uch xonali toq son. ")

else:
    print(" \n1<N<999 oraliqdagi sonni kiriting ")


k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))

while k>0:
  n = input("  \n1 < N < 999 Son kiriting: N =  ")
  a = len(n)

  if n.isdigit() and int(n) > 0 and int(n)<=999:
    if  a == 1 and int(n)%2==0:
      print(" \nSiz kiritgan son bir xonali juft son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))


    elif  a == 1 and int(n)%2 != 0:
      print(" \nSiz kiritgan son bir xonali toq son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))

    elif  a == 2 and int(n)%2 == 0:
      print(" \nSiz kiritgan son ikki xonali juft son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))

    elif  a == 2 and int(n)%2 != 0:
      print(" \nSiz kiritgan son ikki xonali toq son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))

    elif  a == 3 and int(n)%2 == 0:
      print(" \nSiz kiritgan son uch xonali juft son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))

    elif  a == 3 and int(n)%2 != 0:
      print(" \nSiz kiritgan son uch xonali toq son. ")
      k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))


  else:
    print(" \n1<N<999 oraliqdagi sonni kiriting ")
    k = int(input("\n\n\nDasturdan yana  foydalanishni istasangiz u holda  1 ni bosing . \n  Dasturdan chiqishni istasangiz  0  ni bosing. "))


input()
