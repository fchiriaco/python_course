#le istruzioni condizionali determinano il flusso del programma in base ai risultati di un test sui dati

#esempio che verifica se un numero è positivo o negativo
a = input("Scrivi un numero: ") 
numero = float(a)
if numero > 0:
    print(f"{numero} è positivo")
elif numero < 0:
    print(f"{numero} è negativo")
else:
    print("Il numero che hai inserito è 0 ")


#versione 2 
numero = float(input("Scrivi un numero: ")) 
if numero > 0:
    print(f"{numero} è positivo")
elif numero < 0:
    print(f"{numero} è negativo")
else:
    print("Il numero che hai inserito è 0 ")

#esempio che testa se un numero intero è divisibile per 2
numero = int(input("Scrivi un numero intero: ")) 
if numero%2 == 0:
    print(f"{numero} è pari")
else:
    print(f"{numero} è dispari")

#esempio prezzo scontato del 10% se è compreso tra 50 e 70 euro, del 20% se maggiore di 70 euro
prezzo = float(input("Prezzo prodotto: "))
if (prezzo >= 50) and (prezzo <= 70):
    nuovo_prezzo = prezzo*0.9
    print(f"Prezzo da pagare: {nuovo_prezzo}")
elif prezzo > 70:
    nuovo_prezzo = prezzo*0.8
    print(f"Prezzo da pagare: {nuovo_prezzo}")
else:
    print(f"Prezzo da pagare: {prezzo}")


