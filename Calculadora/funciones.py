from Pila import Pila


def infija_a_sufija(expresionInfija):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    # print(type(precedencia))
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()

    for simbolo in listaSimbolos:
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaSufija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.incluir(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.extraer()
        else:
            while (not pilaOperadores.estaVacia()) and (precedencia[pilaOperadores.inspeccionar()] >= precedencia[simbolo]):
                listaSufija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.extraer())
    return " ".join(listaSufija)


##################################################################

def infija_a_prefija(expresionInfija):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia[")"] = 1

    pilaOperadores = Pila()
    listaPrefija= []
    listaSimbolos = expresionInfija.split()

    for simbolo in reversed(listaSimbolos):
        # print(simbolo)
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaPrefija.append(simbolo)
        elif simbolo == ')':
            pilaOperadores.incluir(simbolo)
            # print(simbolo)
        elif simbolo == '(':
            simboloTope = pilaOperadores.extraer()
            # print(simboloTope)
            while simboloTope != ')':
                listaPrefija.append(simboloTope)
                # print(listaPrefija)
                simboloTope = pilaOperadores.extraer()
        else:
            # print(precedencia[simbolo])
            while (not pilaOperadores.estaVacia()) and (precedencia[pilaOperadores.inspeccionar()] >= precedencia[simbolo]):
                listaPrefija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaPrefija.append(pilaOperadores.extraer())
    return " ".join(reversed(listaPrefija))
                

# print(infija_a_prefija("( 6 + 4 ) * 8 ( 7 + 4 )"))



##################################################################


def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        if simbolo in "0123456789":
            pilaOperandos.incluir(int(simbolo))
            # print(simbolo)
        else:
            operando2 = pilaOperandos.extraer()
            #print(operando2)
            operando1 = pilaOperandos.extraer()
            # print(operando1)
            # print(simbolo)
            resultado = hacerAritmetica(simbolo, operando1, operando2)
            # print("resultado: ", resultado)
            pilaOperandos.incluir(resultado)
    return pilaOperandos.extraer()


def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else:
        return operandoIzquierda - operandoDerecha


#print(evaluacionNotacionSufija('7 8 + 3 2 + /'))

# expresion = input()
# print("Infija: ", expresion)
# print("Posfija: ",infija_a_sufija(expresion))
# print("Prefija: ",infija_a_prefija(expresion))
# expresionSufija = infija_a_sufija(expresion)
# try:
#     print("Resultado: ",evaluacionNotacionSufija(expresionSufija))
# except IndexError:
#     print(expresion)
# print(infija_a_prefija("( 6 + 4 ) * 8 ( 7 + 4 )"))


# print(infija_a_sufija("A * B + C * D"))
# print(infija_a_sufija("( A + B ) * C - ( D - E ) * ( F + G )"))
