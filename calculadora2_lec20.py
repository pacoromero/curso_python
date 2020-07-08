#Práctica de la Lección 20.

print(" ")
print(" ")
print("CALCULADORA CON UNA SOLA VARIABLE!! \n")

print(" ")

print("************************")
print("**  MENU DE OPCIONES  **")
print("************************")
print("    1. Suma")
print("    2. Resta")
print("    3. Multiplicación")
print("    4. División")
print("    5. División entera")
print("    6. Exponenete")
print("    7. Módulo o resto \n")

numero = int(input("Elige la opcion deseada: "))
print(" ")

if numero == 1:

	print("Has elegido la operación de suma. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero += int(input("Introduce el valor del segundo número: "))
	print("El resultado de la suma es: ", numero)

elif numero == 2:

	print("Has elegido la operación de resta. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero -= int(input("Introduce el valor del segundo número: "))
	print("El resultado de la resta es: ", numero)

elif numero == 3:

	print("Has elegido la operación de Multiplicacion. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero *= int(input("Introduce el valor del segundo número: "))
	print("El resultado de la Multiplicación es: ", numero)

elif numero == 4:

	print("Has elegido la operación de división. \n")
	numero = float(input("introduce el valor del primer número: "))
	numero /= float(input("Introduce el valor del segundo número: "))
	print("El resultado de la división es: ", round(numero, 2))

elif numero == 5:

	print("Has elegido la operación de división entera. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero //= int(input("Introduce el valor del segundo número: "))
	print("El resultado de la división entera es: ", numero)

elif numero == 6:

	print("Has elegido la operación de elevación de potencia. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero **= int(input("Introduce el valor del segundo número: "))
	print("El resultado de la potencia es: ", numero)

elif numero == 7:

	print("Has elegido la operación para obtener el resto de una división. \n")
	numero = int(input("introduce el valor del primer número: "))
	numero %= int(input("Introduce el valor del segundo número: "))
	print("El resultado del módulo o resto es: ", numero)

else:
	print ("La opción elejida no existe.")
