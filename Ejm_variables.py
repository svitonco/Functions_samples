def calcular (a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b != 0:
         return a/b
        else:
            return "error, no es posible dividir entre 0"
    else:
        return "valor ingresado no es válido"
a = float(input("introduzca un numero: "))
b = float(input("introduzca un numero: "))
operacion = input("Introduzca el signo de la operacion deseada (+-*/)")

resultado = calcular (a, b, operacion)
print (f"Resultado de la operacion: {resultado}")
print (f"este es el {resultado*2}")

