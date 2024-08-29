from contactos.busqueda import *
from contactos.gestion import *

print("Bienvenido a las Amarillas de PubliGuias\n")
print("------------------------\n")
print("Estos son los contactos disponibles:")

def mostrarlista():
	for i in range(len(lista_contactos)):
		print(f"{lista_contactos[i][0]}, {lista_contactos[i][1]}")

mostrarlista()

def opcion():
	aux=int(input("¿Deseas agregar un contacto? : |1-Si| |2-No| "))
	return aux
opcion=opcion()
if (opcion==1):
	name=input("Ingrese nombre: ")
	correo=input("Ingrese correo: ")
	agregar_contacto(name,correo)

print("------------------------\n")
print("Esta es la nueva lista: \n")
mostrarlista()
print("------------------------\n")

def opcion2():
	aux=int(input("¿Deseas buscar un contacto? : |1-Si| |2-No| "))
	return aux
opcion2=opcion2()
if (opcion2==1):

	name=input("Ingrese nombre:")
	print("------------------------\n")
	buscar_contacto(name)
print("------------------------\n")
print("No vuelva. Saludos")








		




