#inicializmos variables en cero
num1 = 0
factor1 = 0
factor2 = 0
factor3 = 0

#funcion para determinar el factor y ver que sonido de gota tiene
def factor(num1):
    #calculamos el modulo de cada numero para ver si tiene factor
    factor1 = num1%7
    factor2 = num1%3
    factor3 = num1%5
    if factor1 == 0:
        print("Ploc")
    if factor2 == 0:
        print("Plic")
    if factor3 == 0:
        print("Plac")
    if factor1 != 0 and factor2 !=0 and factor3!=0:
        print(num1)

#introdcimos por teclado el num a calcular
num1 = int(input("Introduzca un numero para comprobar factores y sonidos de gotas: "))
factor(num1)

