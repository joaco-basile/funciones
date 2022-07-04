import matplotlib as pyplot

def f1(x):
    return eval(input("ingrese la func"))


def split_terminos(function: str):
    terminos=[]
    for _ in range(function.count('(')):
        
        print("Funcion:",function)
        left = function.rfind('(')
        print("Lugar donde se abre el parentesis",left)
        relativo = function[left:].find(')')
        right = left + relativo + 1
        print("Lugar donde se cierra el parentesis",right)
        terminos.append(function[left:right])
        function = function[:left]+function[right:]
        print("Terminos",terminos,"\n\n")
    terminos.append(function)
    return terminos

def calcular_punto():
    a = f1(2)
    print(a)

def graficar_funcion():
    # Valores del eje X que toma el gráfico.
    x = range(-10, 15)
    # Graficar ambas funciones.
    pyplot.plot(x, [f1(i) for i in x])
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    # Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    # Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")
    # Mostrarlo.
    pyplot.show()

calcular_punto()