"""
Il ciclo for è lo strumento principale di Python per iterare su una collezione. 
Scorre ogni elemento di una sequenza, uno alla volta, ed esegue il blocco di codice indentato per ciascuno di essi. 
La sequenza può essere una lista, una stringa, un intervallo di numeri o qualsiasi altro oggetto iterabile.
"""

#esempio 1 - iterare una lista
lista = [1,2,3,4,5,6,7,8]
for i in lista:
    print(i*2)

#esempio 2 - iterare una string
parola = "Python"
for carattere in parola:
    print(carattere)

#esempio 3 - iterazione numerica
for i in range(5):
    print(i)

#in questo esempio si chiede di iterare da 2 a 12 estremo escuso
for i in range(2,12):
    print(i)

#in questo esempio si chiede di iterare i numeri da 0 a 10 usando un incremento di 2 ad ogni passo
#stamperà 0,2,4,6,8
for i in range(0,10,2):
    print(i)

#esempio 4 - enumerare
frutta = ["mela", "banana", "pera"]

for i, frutto in enumerate(frutta):
    print(f"{i + 1}. {frutto}")

"""
Il ciclo while ripete un blocco di codice finché una condizione rimane vera. 
A differenza di un ciclo for normale, che sa quanti elementi itererà, 
un ciclo while normale continua indefinitamente finché qualcosa non cambia la condizione in falsa.
"""
#esempio 1 - semplice contatore
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print("Finito")

#esempio 2 – ciclo infinito
while True:
    risposta = input("Digita  'q'  per uscire: ")
    if risposta == "q":
        print("Addio!")
        break
    else:
	    print("Sei ancora dentro il ciclo")

#esempio 3 - stampa solo i numeri dispari
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)


#esempio 4 - elaborazione ordini di vendita
orders = [
    {"id": 1, "product": "Laptop", "amount": 850, "status": "delivered"},
    {"id": 2, "product": "Mouse", "amount": 15, "status": "delivered"},
    {"id": 3, "product": "Keyboard", "amount": 50, "status": "cancelled"},
    {"id": 4, "product": "Monitor", "amount": 120, "status": "delivered"},
]

total = 0

for i, order in enumerate(orders, start=1):
    if order["status"] == "cancelled":
        print(f"{i}. [CANCELLATO] {order['product']}")
        continue
    total += order["amount"]
    print(f"{i}. {order['product']} - Euro {order['amount']:,}")

print(f"\nTotal (consegnato): Euro {total:,}")
