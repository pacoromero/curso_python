#ejercicio con lista

lista = [1,2,4,5,6]
lista.append(7) #Agrega el 7 al final de la lista
lista.append("Paco") #Agrega  Paco al final de la lista.
lista.insert(2,3)  #inserta el valor 3 en la posición 2 de la lista, si quitamos el 3 de la lista, lo añadirá cuando ejecutemos.
lista.extend([7,8,9]) 
print(3 in lista) #mostrará True o False si está o no el valor de 3 en la lista 
print(linsta.index(5)) #Retorna la posición del indice donde se encuentra el número 5
print(lista.count(1)) #nos va a contar cuantas veces está el valor 1 en la lista.
lista.pop() '''si está sin nada en el paréntesis la funcion pop elimina el último valor de la lista, 
si introduces un valor tú, eliminará el indice que le indiques (AFECTA AL INDICE no AL VALOR.) '''
lista.remove() '''Elimina el valor que le indiques'''
lista.clear() '''elimina todos los elementos de la lista'''
lista.reverse() '''para invertir la lista'''

lista = [1,2,4,5,6]*3 '''triplica la lista'''
lista =[5,4,7,9,0,-3,2]
lista.sort() '''ordena los valores de la lista'''
lista.sort(reverse=True) '''Ordena la los valores de la lista de Mayor a Menor'''

print(lista)

print(lista)

