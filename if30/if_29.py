n = int(input( "Faqat Butun Son kiriting: N =  "))

if n> 0 and n%2 == 0:
  print(" Berilgan Son  musabat juft son. ")
elif n < 0 and n%2 == 0:
  print(" Berilgan Son manfiy juft son. ")
elif n < 0 and n%2 != 0:
  print(" Berilgan Son manfiy toq son. ")
elif n > 0 and n%2 != 0:
  print(" Berilgan Son musbat toq son. ")

else:
  print(" Berilgan Son no'l son. ")

input()
