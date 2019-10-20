# sir = "ACADEMIE"
# print(sir[0])
# print(sir[-1])
# print(sir[1:])
# print(sir[1:4])
# print(sir[len(sir):2:-1])
# print(sir[-3:-7:1])
# print(sir[::])
# print(sir[::-1])

# sir = input("Dati un sir de caractere: ")
# invers = sir[::-1]
# if sir == invers:
#     print("Sirul introdus este palindrom")
# else:
#     print("Sirul nu este palindrom!")

# print(len(sir))
# print(sir.__len__())

# print(sir[len(sir) -  1]) # <=> print(sir[-1])

# print(sir * 3)

# sir_util = "sir util procesarii \n \t  "
# print(sir_util)
# print(sir_util.rstrip())
# sir_util = "               informatie utila"
# print(sir_util.lstrip())
#
# sir_text = "night of poker888"
# print(sir_text.rstrip("888"))

# sir = "%s academy preda cursuri de %i ani" %('telacad', 12)
# sir = "{0} academy preda cursuri de {1} ani".format('telacad', 10)
# sir = "{} academy".format('telecom')
# print(sir)

#Lista este colectie de date neomogene
# lista = [123, 'telacad', '888', True]
# print("ID-ul listei initial: {}".format(id(lista)))
# lista[0] = 457
# print("ID-ul listei dupa modificare: {}".format(id(lista)))
# lista[0] = 'academy'
#
# lista.append("new value")
# last_element = lista.pop()
# sec_element = lista.pop(1)
#
# print(last_element)
# print(sec_element)
#
# lista_nr = [1, 2, 3, 68, -1, 2]
# lista_nr.sort()
# lista.reverse()

# lista = ['telacad', 123, 'abc']
# for val in lista:
#     print(val, end = " ")
#
# print("\n", end = " ")
# print("-" * 20)
# for l in range(len(lista)):
#     print(lista[l], end = " ")

# # Afisati liste cu numere/pare, impare
# # Numerele se citesc de la tastatura
# #1
# nr_pare = []
# nr_impare = []
# nr_val = int(input("Numar elemente: "))
# lista = []
# i = 1
# while True:
#     valoare = int(input("Valoare: "))
#     lista.append(valoare)
#     if i == nr_val:
#         break
#     i += 1
# print(lista)
#
# for nr in lista:
#     if nr % 2 == 0:
#         nr_pare.append(nr)
#     else:
#         nr_impare.append(nr)
#
# print("Numere pare: ", nr_pare)
# print("Numere impare: ", nr_impare)

# #2
# nr_pare = []
# nr_impare = []
#
# nr_val = int(input("Numarul de valori de sortat: "))
# for i in range(nr_val):
#     val = int(input("Valoarea {}: ".format(i + 1)))
#
#     if (val % 2 == 0):
#         nr_pare.append(val)
#     else:
#         nr_impare.append(val)
#
# print(nr_impare)
# print(nr_pare)


# lista = [123, 577, "telacad"]
# del lista[0]
# print(lista)

# matrice = [ [1, 2, 3], [4, 6], [7, 8, 9, 10]]
# # print(matrice[0][1])
# for i in matrice:
#     for j in i:
#         print(j, end = " ")
#     print("\n", end = "")

# tuplu = (123, "lala", "telecom academy", True)
# print(type(tuplu))
# var = (123)
# print(type(var)) #int
# var = (123, )
# print(type(var)) #tuple

# sir = "cursul de python fundamentals"
# print("python" not in sir)
#
# lista = ['telacad', 'systems', 123, True]
# print(True not in lista)
# print('telacad' in lista)
#
# tuplu = ('limbaj', 56, 123, 2)
# print(10 in tuplu)

# set_unic = {1, 2, 79, 90, 123, 78, 1, 2}
# print(set_unic)
# print(type(set_unic))
# set_2 = set(['a', 'b', 'c', 'Z', 'a'])
# print(set_2)

# set_nou = {'a', 'telacad', 'metro', 'systems'}
# set_nou.add("telacad2007")
# set_nou.update(['b', 'telacad', 'ceva_nou' ])
# print(set_nou)

# set_nou.remove("bucuresti") - KeyError pentru ca elementul cautat nu se afla in set

# set_nou.discard("Bucuresti") #nu am eroare chiar daca elementul nu se afla in set

# nr_valori = int(input("Ba, cate valori vrei? "))
# val = []
# i = 0
# while i < nr_valori:
#     valoare = int(input("Introduceti valoarea {}: ".format(i + 1)))
#     val.append(valoare)
#     i += 1
#
# total = len(val)
# unice = len(set(val))
# print("Valori totale: ", val)
# print("Valori unice: ", set(val))
# print("{} % unice".format(unice / total * 100))

# nr_valori = int(input("Ba, cate valori vrei? "))
# lista = []
# for i in range(nr_valori):
#     valoare = int(input("Valoare {}: ".format(i + 1)))
#     lista.append(valoare)
# print(lista, "toate valorile")
# print(set(lista), "valori unice")
# nr_total = len(lista)
# nr_unice = len(set(lista))
# print(nr_total)
# print(nr_unice)
# print(nr_unice / nr_total * 100)

names_and_ages = [('Alice', 25), ('Ionut', 89), ('Bob', 25), ('Karen', 33)]
dictionar = dict(names_and_ages)
# print(dictionar)
#
# dictionar.update({'Alice': 33, 'Mark':34})
# print(dictionar)
#
# dictionar.update({True : "lalala"})
# print(dictionar)
# dictionar['Alice'] = 77
# print(dictionar['Alice'])
# print(dictionar.update({"Alice": ""}))
# print(dictionar)
# print(dictionar['Cheie_inexistenta']) - va returna KeyError pentru ca nu exista in dict-ul de mai sus
# print(list(dictionar.values()))
# for value in dictionar.values():
#     print(value, end = " ")
# print("\n")
# for keys in dictionar.keys():
#     print(keys, end = " ")
# print("\n")
#
# print(25 in dictionar)
# print('Alice' in dictionar) #in cauta in cheile dictionarului, nu in valori

# print(dictionar.items())
# for k, v in dictionar.items():
#     print("Cheia este: {0} -> Valoarea este: {1}".format(k, v))
#
# del dictionar['Alice']
# print(dictionar)

import day_3_part_2 as curs
print(curs.invers("sir aleator de caractere"))