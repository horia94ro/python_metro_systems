# a = 10
# b = 25
#
# c = a == b
# print("c: ", c)
#
# d = a >= b
# print("d: ", d)
#
# e = c != d
# print("e: ", e)
#
# f = a < b < 50
# # a < b
# # b < 50
# print("f: ", f)
#
# g = a > 9 > 50
# print("g: ", g)
#
# h = (a > 9) and (9 > 50)
# print("h: ", h)
# #Sintaxele de verificare g si h sunt identice
#
# i = not h
# print("i: ", i)
#
# j = (c == d) or (f == e)
# print("j: ", j)

# x = input("X: ")
# x = float(x)
# y = input("Y: ")
# y = float(y)
# operatie = input("Operatia dorita de dvs: ").lower()
# rez = None
# if operatie == "adunare":
#     rez = x + y
# elif operatie == "scadere":
#     rez = x - y
# elif operatie == "inmultire":
#     rez = x * y
# elif operatie == "impartire":
#     rez = x / y
# else:
#     print("Operatia selectata este invalida!")
#
# print(rez)

# ora = int(input("Introduceti ora dorita: "))
#
# if (ora >= 0) and (ora < 24):
#     if (ora > 6) and (ora <= 11):
#         print("Buna dimineata")
#     elif (ora >= 12) and (ora < 18):
#         print("Buna ziua!")
#     elif (ora >= 18 and ora < 22):
#         print("Buna seara!")
#     else:
#         print("Noapte buna!")
# else:
#     print("Valoarea orei nu se afla pe ceas")

# a = 10
# while a > 0:
#     if a == 5:
#         break
#     print(a)
#     a = a - 1
#
# print("-----------------------------")
# a = 10
# while a > 0:
#     a -= 1
#     if a == 5:
#         continue
#     print(a)

# for i in range(10):
#     print(i, end = " ")
#
#range() primeste ca si argumente - punct de start/stop/step
# for i in range(1, 20, 3):
#     print(i, end = " ")

# for i in range(20, 1, -1):
#     print(i, end=" ")

#range() - nu primeste keyword arguments - valorile se dau direct
# for i in range(start = 5, stop = 10, step = 2):
#     print(i)

# cuvinte = ['telecom', 'academy', 'lista', 'cursuri', 'variata']
# for cuv in cuvinte:
#     print(cuv, len(cuv))

# for i in range(len(cuvinte)):
#     print(i, cuvinte[i])
#
# sir = 'metro systems academy'
# for i in sir:
#     print(i)

# while 1:
#     cuvant = input("Introdu un cuvant: ").lower()
#     if cuvant == 'telacad':
#         break
#     else:
#         print("Cuvantul introdus nu este corect!")
# print("Sfarsitul programului")
#
# cuvant = input("Dati cuvant: ").lower()
# while cuvant != "telacad":
#     cuvant = input("Dati cuvant: ")
# print("Sfarsitul programului")

# nr = int(input("Introduceti un numar: "))
# suma = 0
# while nr < 2:
#     nr = int(input("Introduceti un numar > 2: "))
#
# for i in range(1, nr + 1):
#     suma = suma + i
#
# print(suma)

# while True:
#     nr = int(input("Dati un numar: "))
#
#     if nr > 2:
#         rez = 0
#         for i in range(1, nr + 1):
#             rez += i
#         print("Suma numerelor este: ", rez)
#         break

# lista = ["telacad", "peste 12 ani vechime", "predare", "cursuri online"]
# while 1:
#     cuv = input("Introduceti un cuvant").lower()
#     if cuv != "telacad":
#         continue
#     else:
#         for item in lista:
#             print(item, end = " ")
#         break

# x = 15.0
# if isinstance(x, int):
#     print("Numarul este intreg")
#     print("Rezultat: ", x + 3)
# elif isinstance(x, float):
#     print("Numarul este real")
#     print("Rezultat: ", x / 2)
# elif isinstance(x, complex):
#     print("Numarul este imaginar")
#     print("Parte reala: ", x.real)
#     print("Parte imaginara:", x.imag)
#     print("Modul:", abs(x))

# x = int(input("Introduceti numarul de verificat: "))
# if x % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este impar")

import math
# x = int(input("Introduceti numarul de verificat: "))
# prim = True
# for i in range(2, int(math.sqrt(x))):
#     if x % i == 0:
#         prim = False
#
# print(prim)

# x = int(input("Introduceti numarul de verificat: "))
# prim = True
# while prim == True:
#     for i in range (2, int(math.sqrt(x))):
#         if x % i == 0:
#             prim = False

# x = int(input("Introduceti numarul de verificat: "))
# nr_div = 0
# for i in range(2, math.floor(x / 2) + 1):
#     if x % i == 0:
#         nr_div += 1
#
# if nr_div == 0:
#     print("Numarul este prim")
# else:
#     print("Numarul nu este prim.")