from .gestion import *
def buscar_contacto(nombre):
	nombres=[]
	indice=[]
	for i in lista_contactos:
		aux2=("")
		aux=i[0]

		for j in aux:
			if j!=(" "):
				aux2+=j
			else:
				break
		nombres.append(aux2)
	for i in range(len(nombres)):
		if nombre==nombres[i]:
			indice.append(i)

	for i in indice:
		print(f"Los Contactos encontrados son {lista_contactos[i][0]} - {lista_contactos[i][1]}")