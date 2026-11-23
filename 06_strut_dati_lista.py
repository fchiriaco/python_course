"""
Le liste sono molto simili agli array presenti in altri linguaggi di programmazione. 
Permettono di riunire più valori, anche di tipo diverso, sotto uno stesso nome e richiamarli singolarmente mediante un indice.
Gli indici di una lista partono da 0
"""

#dichiarazione e stampa di una lista
mia_lista = [1,2,3,4,5,6]
mia_lista2 = ["Casa",3,True,5.7]
print(mia_lista)
print(mia_lista2)

#iteriamo gli elementi di mia_lista e stampiamo in output il quadrato di ciascuno di essi
for i in mia_lista:
    print(i**2)

#calcoliamo la media aritmetica di mia_lista
somma = 0
n_elementi = len(mia_lista)
for numero in mia_lista:
    somma += numero
media = somma/n_elementi
print(f"la media di {mia_lista} è {media} " )

#stampiamo il secondo elemento della lista
mia_lista[1]
#stampiamo l'ultimo elemento della lista
mia_lista[len(mia_lista)-1] 
#oppure
mia_lista[-1]  #quando si usano gli indici negativi si parte da destra 
#stampiamo il penultimo elemento
mia_lista[-2]
#Modifichiamo il terzo elemento della lista
mia_lista[2] = 8

#metodi per aggiungere o rimuovere elementi alla lista
products = ["Laptop", "Mouse"]

products.append("Keyboard")
print(products)

products.insert(1, "USB Hub")
print(products)

products.remove("Mouse")
print(products)

removed = products.pop()
print(removed)
print(products)

#ordinamento e ricerca
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#ordina gli elementi della lista
numbers.sort()
#ordina la lista in ordine decrescente
numbers.sort(reverse=True)
print(numbers)
#stampa la lista al contrario (attenzione non ordina in ordine decrescente)
numbers.reverse()
print(numbers)
#restituisce True se laptop è contenuto in products
print("Laptop" in products)
#stampa il numero di laptop presenti in lista
print(products.count("Laptop"))
#stampa l'indice di "USB Hub"
print(products.index("USB Hub"))

"""
List Compreheshion

Una list comprehension è un modo conciso per creare una nuova lista applicando un'espressione a ciascun elemento di una sequenza esistente, 
filtrando facoltativamente gli elementi in base a una condizione. 
Sostituiscono da tre a cinque righe di codice di ciclo con un'unica riga leggibile.
"""

#modo classico lungo (che si è costretti ad usare in altri linguaggi)
prices = [850, 150, 750, 282]
with_tax = []
for p in prices:
    with_tax.append(p * 1.22)
print(with_tax)

#modo stringato possibile in python
with_tax = [round(p * 1.22,2) for p in prices]
print(with_tax)

#Filtrare i dati

prices = [850, 150,  750, 280]

expensive = [p for p in prices if p > 500]
print(expensive)


"""
Slicing: peculiarità molto comoda in python. 
Permette di restituire porzioni di una lista (come se la affettassimo 😊).
"""

lista = [1,2,3,4,5,6,7,8,9]

dal_secondo_al_quinto = lista[1:5] #restituisce la lista con gli elementi che hanno indice compreso tra 1 e 4 
print(dal_secondo_al_quinto)

fino_al_terzo = lista[:3] #se non si specifica il primo elemento parte dall'inizio
print(fino_al_terzo)
dal_secondo_alla_fine = lista[1:]
print(dal_secondo_alla_fine)

da_terzultimo_al_penultimo = lista[-3:-1] #qui abbiamo usato gli indici negativi
print(da_terzultimo_al_penultimo)




