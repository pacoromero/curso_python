#Conjunción

print("Conjuncion (and)")

num_uno =  int(input("Introduce un número a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " cumple con la condición.\n")

else:
    print("El número ", num_uno, " no cumple la condición.\n")

#Disyunción
    print("Disyunción (or)")

palabra = input("Para cumplir con la condición escriba 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido. \n")

else:
    print("La condición no se ha cumplido. \n")

#Negación

print ("Negación (not)")

int(input("Introduce un numero igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de cinco y si cumple la condición. \n")

else:
    print("\n El numero es igual que 5 y NO cumple la condición.\n")
