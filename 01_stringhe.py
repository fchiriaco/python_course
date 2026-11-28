#metodi per le stringhe

#Metodi di gestione degli spazi bianchi e delle maiuscole/minuscole

raw = "  Hello, World!  "

print(raw.strip()) #stampa la stringa eliminando gli spazi iniziali e finali
print(raw.lstrip()) #stampa la stringa eliminando gli spazi iniziali (l sta per left)
print(raw.rstrip()) #stampa la stringa eliminando gli spazi finali (r sta per right)
print(raw.lower()) #stampa la stringa in minuscolo
print(raw.upper()) #stampa la stringa in minuscolo

name = "francesco chiriaco" 
print(name.title()) #stampa Francesco Chiriaco (scrive in maiuscolo la prima lettera di ogni parola)
print(name.capitalize()) #stampa Francesco chiriaco (scrive in maiuscolo la prima lettera della prima parola)

#replace e concatenamento dei metodi
raw_price = "Euro 8.500"
cleaned = raw_price.replace("Euro ", "").replace(".", "")
price = int(cleaned)
print(price)

messy = "  ROSSI STEFANO  "
normalized = messy.strip().lower().title()
print(normalized)

#divisione e unione 
#split()
csv_line = "Francesco,Agropoli,10,active"
parts = csv_line.split(",")
print(parts)
print(parts[0])
print(parts[2])

path = "/home/user/documents/report.csv"
segments = path.split("/")
print(segments)
print(segments[-1])

#join()
parts = ["Francesco", "Agropoli", "10", "active"]
csv_line = ",".join(parts)
print(csv_line)

words = ["Python", "is", "great"]
sentence = " ".join(words)
print(sentence)

filename_parts = ["2026", "04", "30", "report"]
filename = "_".join(filename_parts) + ".csv"
print(filename)

#ricerca di stringhe
email = "rossi@example.com"

print("@" in email)
print("@" not in email)
print(email.startswith("rossi"))
print(email.endswith(".com"))
print(email.find("@"))
print(email.find("xyz"))

#specificatori di formato f-string
products = [
    ("Laptop", 850),
    ("Mouse", 10),
    ("Keyboard", 70),
]

print(f"{'Product':<25} {'Price':>15}")
print("-" * 42)
for name, price in products:
    print(f"{name:<25} {price:>15,.0f}")

#precisione decimale e percentuale
tasso = 0.1156
pi = 3.141592653589793
punteggio = 0.875

print(f"Rate: {tasso:.2%}")
print(f"Rate: {tasso:.4f}")
print(f"Pi:   {pi:.3f}")
print(f"Score: {punteggio:.1%}")

#allineamento
title = "Report delle vendite"
print(f"{title:=^40}")
print(f"{'':=^40}")
print(f"{'Totale':>40}")

#pulizia dei dati
raw_records = [
    "  Laptop | Euro 850 | Roma  ",
    " MOUSE | Euro 10 | Milano ",
    "Keyboard  | Euro 75  | Napoli",
]

cleaned = []
for record in raw_records:
    parts = record.strip().split("|")
    product = parts[0].strip().title()
    price_str = parts[1].strip().replace("Euro ", "").replace(".", "")
    price = int(price_str)
    city = parts[2].strip().title()
    cleaned.append({"product": product, "price": price, "city": city})

for item in cleaned:
    print(f"{item['product']:<25} Euro {item['price']:>12,}  {item['city']}")

