print("Introduce dos números para comparar: \n")
num_uno = int(input("Introduce el primer número de la comparación: \n"))
num_dos = int(input("Introduce el segundo número de la comparación: \n"))

print("\n Los numeros a comparar son: ",  num_uno, " y ", + num_dos, ".\n")

if num_uno != num_dos:
    print("Son diferentes...\n")
if num_uno > num_dos:
    print("Es mayor...\n")
if num_uno < num_dos:
    print("Es menor...\n")
if num_uno >= num_dos:
    print("Es mayor o igual...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno == num_dos:
    print("Son iguales...")

else:
    print("\n Gracias.")

