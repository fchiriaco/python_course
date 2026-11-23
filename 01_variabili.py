"""
 In python, a differenza di altri linguaggi, 
 quando si dichiara una variabile non è necessario
 specificare il tipo, questo viene riconosciuto automaticamente dal sistema.
"""
a = 2   #variabile di tipo intero - int
b = 3.5 #variabile di tipo decimale - float
c = "Sono una stringa"  #variabile di tipo stringa - str

#Vediamo qualche esempio con le variabili di tipo numerico
x = 2
y = 3
z = x + y
print(f"{x} + {y} = {z}\n")
p = 2.5
q = 3
t = p*q
print(f"{p}*{q} = {t}\n")

n = 13
m = 5
divisione_intera =  n//m
divisione = n/m
resto = n%m
print(f"Divisione intera tra {n} e {m} = {divisione_intera}\n")
print(f"Divisione in Q tra {n} e {m} = {divisione}\n")
print(f"Il resto della divisione tra {n} e {m} è {resto}\n")

potenza = m**3
print(f"{m} elevato a {3} = {potenza}\n")

#vediamo qualche esempio con le stringhe
nome = "Francesco"
saluto = "Ciao"

frase = saluto + " " + nome
print(frase)

#casting delle variabili
print(f"\nvalore di m prima del casting: {type(m)}\n")
m = str(m)
print(f"valore di m dopo del casting: \"{type(m)}\"\n")

#Stringhe multilinea 

bio = """Questa è una
multi-line string
in Python."""
print(bio)

#variabili di tipo booleano
a = True
b = False

print(f"\na or b = {a or b}")

print(f"\na and b = {a and b}\n")





