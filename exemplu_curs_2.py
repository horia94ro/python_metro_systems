# import math
#
# a1 = 10.5
# print(round(a1))
#
# a1 = 10.3
# print(math.ceil(a1))
# print(math.floor(a1))
#
# sir = """
#     SIR DE CARACTERE
#     CARE E FOARTE LUNG
#     SSI NU AR INCAPEA
#     PE O SINGURA LINIE
# """
# print(sir)
# sir = "TELECOM\tACADEMY"
# print(sir)

# a = ( (9 > 7) and (5 < 10) )
# a = not a
# print(a)
# a = 10
# b = 5
# if  a < b:
#     print("HELLO WORLD")
#     print("ALTA INSTRUCTIUNE")

# if True:
#     print("Conditie mereu adevarata")
# else:
#     print("Cod unreachable")

# if bool("telacad"):
#     print("Conditia este adevarata")

# inaltime = 35
#
# if inaltime > 50:
#     print("Inaltimea este mai mare decat 50!")
# else:
#     if inaltime < 20:
#         print("Inaltimea este mai mica decat 20")
#     else:
#         if inaltime == 10:
#             print("Inaltimea este de 10")
#         else:
#             print("Inaltimea este intre 20 si 50!")
#
# if inaltime > 50:
#     print("Inaltimea este mai mare decat 50")
# elif inaltime < 20:
#     print("Inaltimea este mai mica decat 20")
# elif inaltime == 10:
#     print("Inaltimea este de 10")
# else:
#     print("Inaltimea este intre 20 si 50!")

anotimp = input("Baga anotimpul: ").lower()

if anotimp == "vara":
    print("cald")
elif anotimp == "toamna" or "primavara":
    print("ploo")
elif anotimp == "iarna":
    print("frig")
else:
    print("Valoare incorecta!")




