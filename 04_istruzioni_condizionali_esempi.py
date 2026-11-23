#esempio 1
punteggio = 85
if punteggio >= 90:
   voto = "A"
elif punteggio >= 80:
    voto = "B"
elif punteggio >= 70:
    voto = "C"
else:
    voto = "F"

print(f"Punteggio: {punteggio}, Voto: {voto}")

#esempio 2
frutta_in_negozio = ["pera","mela","banana","uva"]
frutto = input("Scrivi il nome di un frutto: ")
if (frutto in frutta_in_negozio):
    print("Il cliente può essere servito")
else:
    print(f"spiacenti non abbiamo {frutto} in negozio, torni domani")
