#Programa de gestión de vacaciones de la empresa Rappi.
print("******************************************************")
print("Bienvendios al programa de gestion de vacaciones (PGV)")
print("****************************************************** \n")

nombre = input("Por favor introduce tu nombre: \n")
print(" \n MENÚ DEPARTAMENTOS:")
print("--------------------")
print("(1) - ATENCIÓN AL CLIENTE.")
print("(2) - LOGISTICA.")
print("(3) - GERENCIA.")

clv = int(input('\nBuenas ' + nombre + '. Por favor introduce tu clave de departamento: \n'))
if clv == 1:
    print("\n Has introducido un 1, eres del Dpto. de Atención al cliente. \n")
    ant = float(input("Ahora introduce los años que llevas en la empresa: \n"))

    if ant == 1 and ant < 2:
        print(nombre, "Vas a recibir 6 días de vacaciones. \n")
    elif ant >=2 and ant <=6:
        print(nombre, "Vas a recibir 14 días de vacaciones. \n")
    elif ant >=7:
        print(nombre, "Vas a recibir 20 días de vacaciones. \n")
    else:
        print("\n No te corresponden días de vacaciones de momento. \n ")
        
elif clv == 2:
    print("\n Has introducido un 2, eres del Dpto. de Logística.\n")
    ant = int(input("Ahora introduce los años que llevas en la empresa: \n"))
    
    if ant == 1:
        print(nombre, "Vas a recibir 7 días de vacaciones. \n")
    elif ant >=2 and ant <=6:
        print(nombre, "Vas a recibir 15 días de vacaciones. \n")
    elif ant >=7:
        print(nombre, "Vas a recibir 22 días de vacaciones. \n")
    else:
        print("\n No te corresponden días de vacaciones de momento. \n ")
elif clv == 3:
    print("\n Has introducido un 3, eres del Dpto. de Gerencia. \n")
    ant = int(input("Ahora introduce los años que llevas en la empresa: \n"))
    
    if ant == 1:
        print(nombre, "Vas a recibir 10 días de vacaciones. \n")
    elif ant >=2 and ant <=6:
        print(nombre, "Vas a recibir 20 días de vacaciones. \n")
    elif ant >=7:
        print(nombre, "Vas a recibir 30 días de vacaciones. \n")
    else:
        print("\n No te corresponden días de vacaciones de momento. \n ")
if clv >3:
    print("La clave introducida es incorrecta.\n ")
else:
    print("Gracias por usar PGV para sus gestiones vacacionales.")
