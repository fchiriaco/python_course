#Un dizionario associa le chiavi ai valori,
#esempio 1
utente = {
    "nominativo": "Mario Rossi",
    "email": "rossi@gmail.com",
    "ruolo": "Editor"
}

print(utente["nominativo"])

#esempio 2
prodotto = {
    "nome": "Laptop ProBook 14",
    "categoria": "Elettronica",
    "prezzo": 800,
    "in_stock": True,
}

print(prodotto["nome"])
print(prodotto["prezzo"])
print(prodotto.get("colore"))
print(prodotto.get("colore", "Nero"))
prodotto["colore"] = "Bianco"
print(prodotto)

#modificare un dizionario
prodotto["prezzo"] = 799
prodotto["marca"] = "ProTech"
del prodotto["in_stock"]
print(prodotto)

#iterare un prodotto
prodotto = {"nome": "Laptop", "prezzo": 800, "categoria": "Elettronica"}
for key in prodotto:
    print(key)

for value in prodotto.values():
    print(value)

for key, value in prodotto.items():
    print(f"{key}: {value}")

#elenchi di dizionari
ordini = [
    {"id": 1, "prodotto": "Laptop", "prezzo": 800, "stato": "consegnato"},
    {"id": 2, "prodotto": "Mouse", "prezzo": 7, "stato": "consegnato"},
    {"id": 3, "prodotto": "Tastiera", "prezzo": 50, "stato": "cancellato"},
    {"id": 4, "prodotto": "Monitor", "prezzo": 200, "stato": "cancellato"},
]

totale_consegnati = sum(o["prezzo"] for o in ordini if o["stato"] == "consegnato")
print(f"Totale consegnati: Euro {totale_consegnati:,}")

cancellati = [o["prodotto"] for o in ordini if o["stato"] == "cancellato"]
print(f"Ordini cancellati: {cancellati}")

#raggruppamento per stato ordine
status_groups = {}
for ordine in ordini:
    stato = ordine["stato"]
    if stato not in status_groups:
        status_groups[stato] = []
    status_groups[stato].append(ordine["prodotto"])
for stato, prodotto in status_groups.items():
    print(f"{stato}: {prodotto}")

#comprehension con i dizionari
prezzi = {"Laptop": 800, "Mouse": 7, "tastiera": 70}

with_tax = {nome: round(prezzo * 1.22,2)  for nome, prezzo in prezzi.items()}
print(with_tax)

costosi = {k: v for k, v in prezzi.items() if v > 500}
print(costosi)


