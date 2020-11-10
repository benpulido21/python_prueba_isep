#declaramos la clase triangulo con el constructor y sus atributos privados
class Triangulo(object):
    def __init__(self):
        self.__a = 6
        self.__b = 10
        self.__c = 6
        #metodo para calcular la altura y area de un triangulo e imprimirlo
    def CalcularArea(self):
        a = self.__a
        b = self.__b
        c = self.__c
        h = a*b/c
        area = b*h/2
        print("El area del triangulo es: ",area)

#instanciamos el clase y objeto y llamamos a la funcion calcular area
calculo = Triangulo()
calculo.CalcularArea()