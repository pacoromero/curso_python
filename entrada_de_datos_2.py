nombre = input("Hola, como te llamas: ")
print("Buenas " + nombre)
edad = int(input("Que edad tienes: " + nombre))
edad = str(edad)
print("Perfecto, te llamaré " + nombre + edad)
print(" ")
print("Ok " + nombre + edad +" Vamos a jugar con los numeros te parece?")

valor_uno = int(input("Elije un numero: "))
valor_dos = int(input("Elije un segundo numero: "))

print("Ahora haremos una suma, resta, multiplicacion y division")

suma = valor_uno + valor_dos
suma = str(suma)
print("El valor de la suma es: ", suma)

resta = valor_uno - valor_dos
resta = str(resta)
print("El valor de la resta es: ", resta)

multiplicacion = valor_uno * valor_dos
multiplicacion = str(multiplicacion)
print("El valor de la multiplicacion es: ", multiplicacion)

division = valor_uno / valor_dos
division = str(division)
print("El valor de la división es: ", division)
