#
"""
Con l'aumentare della lunghezza del codice, la ripetizione diventa un problema. 
Si scrive lo stesso calcolo in tre punti diversi e, quando la formula deve cambiare, 
bisogna cercarla e aggiornarla in tre punti diversi, 
aumentando la probabilità di commettere errori ed di  introdurre bug nel codice.  Le funzioni risolvono questo problema permettendo di scrivere una porzione di logica una sola volta, assegnarle un nome e richiamarla da qualsiasi punto del programma. La logica di una funzione risiede in un unico punto e viene riutilizzata in qualunque altra parte del codice è necessaria, utilizzando il nome ad essa associato e passandole eventuali parametri.
"""

#esempio calcolo area rettangolo
def area_rettangolo(base,altezza):
    area = base*altezza
    return area

#utilizzo della funzione nel programma
base = float(input("Base = "))
altezza = float(input("Altezza = "))
area = area_rettangolo(base,altezza)
print(f"L'area del rettangolo di base {base} e altezza {altezza} è: {area}")

#esempio funzione senza parametri di input e senza return (serve solo a produrre qualche side effect)
def stampa_separatore():
    print("-"*40)

#utilizzo
stampa_separatore()
print("testo tra le due linee di separazione")
stampa_separatore()

#esempio funzione con parametri predefiniti
def get_excerpt(text, length=100):
    if len(text) <= length:
        return text
    return text[:length] + "..."

print(get_excerpt("Testo breve"))
print(get_excerpt("Un testo lungo, ma molto lungo, ma veramente lungo che verrà troncato dopo venti caratteri", 20))

#esempio parametri con nome
def crea_prodotto(nome, prezzo, categoria, in_stock=True):
    return {
        "nome": nome,
        "prezzo": prezzo,
        "categoria": categoria,
        "in_stock": in_stock,
    }

prodotto_a = crea_prodotto("Laptop", 8500000, "Elettronica")
prodotto_b = crea_prodotto(nome="Mouse", prezzo=8, categoria="Accessori", in_stock=False)

print(prodotto_a)
print(prodotto_b)

#funzioni che restituiscono più valori
def analizza_prezzi(prezzi):
    minimo = min(prezzi)
    massimo = max(prezzi)
    prezzo_medio = sum(prezzi) / len(prezzi)
    return minimo, massimo, prezzo_medio

prezzi = [850, 150, 750, 280]
min, max, medio = analizza_prezzi(prezzi)

print(f"Più basso:   Euro {min:,}")
print(f"Più alto: Euro {max:,}")
print(f"Medio: Rp {medio:,.2f}")

#funzione lambda

#definizione normale
def doppio(x):
    return x * 2

#definizione lambda
doppio_lambda = lambda x: x * 2

#stesso risultato sia nel modo standard che con l'uso di lambda
print(doppio(5))
print(doppio_lambda(5))

#esempio di utilizzo nell'ordinamento
products = [
    {"name": "Laptop", "price": 850},
    {"name": "Mouse", "price": 9},
    {"name": "Monitor", "price": 180},
]

products.sort(key=lambda p: p["price"])

for product in products:
    print(f"{product['name']}: Euro {product['price']:,}")


#funzioni con numero di parametri variabile

def log_all(*args):
    for message in args:
        print("LOG:", message)

log_all("starting")
log_all("ready", "set", "go")
log_all()    # anche zero argomenti va bene


#kwargs accetta parametri tipo chiave=valore e li raggruppa in un dizionario
def logger(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)

logger(1, 2, 3, level="warn", tag="api")


