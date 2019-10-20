def suma(x, y):
    return x + y

def rest(x):
    return x % 2

def par_impar(x):
    if x % 2 == 0:
        print("NUMAR PAR")
        return
    else:
        print("NUMAR IMPAR")

def invers(x):
    if len(x) == 0:
        return
    else:
        return x[::-1]

def putere(a, b = 2):
    print(a ** b)

def functie(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

def functie_2(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

functie_2("Horia", academie = "Telacad", adresa = "Apaca", telefon = "021")
# # print(par_impar(10))
# rezultat = invers("telecom academy")
# print(invers(""))
# putere(5)
# putere(10, 3)
# putere(b = 5, a = 7)
functie(1, 2, 3, 4)
functie(1, 2)
functie()


