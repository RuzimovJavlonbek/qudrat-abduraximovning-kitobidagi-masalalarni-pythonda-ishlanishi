
mevalar = [ "Olma" , "Nok" , "Gilos" , " Olcha" ]

mevalar.append("Behi")
c = len(mevalar)
print(c,"  ,  ",mevalar)

urni = list(enumerate(mevalar))
print("\n\n", urni)

del mevalar[4]

print(mevalar)

mevalar[0] ="JAvlonbek"
print(mevalar)

mevalar.insert(0,"RUZIMOV")
print(mevalar)
mevalar.insert(0,"RUZIMOV")
print(mevalar)

mevalar.remove(" Olcha")
print(mevalar)

mashinalar = list(("Malibu", "Tiko", "Spark","Damas","Matiz"))
print(mashinalar)
print('\n\n\n',mashinalar[1:4])

c="salom"
print(c[1],c[2] , c[1:])

for x in mashinalar:
  print(x)


mashinalar = list(("Malibu", "Malibu", "Tiko",
                  "Malibu", "Spark", "Malibu", "Damas", "Malibu", "Matiz", "Malibu",))
if "Ferrari" in mashinalar:
  print("\n\n\n Ha , Ferrari bor")
else:
   print("\n\n\n\nFerrari yo'q.")

print(mashinalar.count("Malibu"))
print()

#mashinalar.clear()
print(mashinalar)

nusxa_mashina = mashinalar.copy()
print(nusxa_mashina)

nusxa_mashina_2 = list(mashinalar)
print(nusxa_mashina_2)

c = nusxa_mashina_2 + mashinalar + mevalar
print(" \n\n\n ",c)


for x in mashinalar:
  mevalar.append(x)

#print(" \n\n\n  \n\n\n ", mevalar)

for x in mevalar:
  print(x)


mevalar.extend(c)
print(mevalar)


a = [ 1,2,3,4,5]
b = [6,7,8,9,10,11,]

a.extend(b)
print(" NATIJA BUU  EXXTEND:::  ", a)

d1 = [12,13,14,15,16,17,18]
d2 = [19,20,21,22,23,24,25,26,27,28,29,30]

for son in d2:
  d1.append(son)

print("\n\n\n Natija FOR append",d1)


d3 = [ 30, 31,32,33,34,35,36,37,38,39,40]
d4 = [41,42,43,44,45,46,47,48,49,50]
d5 = d3 + d4
print("\n\n\n Natija  d5 = d3 + d4 ", d5)


d6 = [1,2,3,4,5,6,7,5,5,5,5]
x = d6.count(5)
print(" \n\n\n SONI = ",x)

x = d6.index(5)
print(" \n\n\n 5 ni indeksi  = ", x)


d7 = [8,1,3,2,9,4,6,5,7,10]
print("\n\n\n" , d7)
d7.sort( )
print("\n" , d7)

poliz = ["olma", "banan", "apelsin", "nok","uzum"]
print("\n\n\n", poliz)
poliz.sort()
print("\n", poliz)



print("\n\n\n", d7)
d7.reverse()
print(d7)

print("\n\n\n", poliz)
poliz.reverse()
print(poliz)



#print(extend(2))
input()
