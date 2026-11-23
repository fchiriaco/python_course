"""
Una tupla è una sequenza immutabile. 
Somiglia a una lista, ma utilizza le parentesi tonde al posto delle parentesi quadre e, una volta creata,
 il suo contenuto non può essere modificato. 
 Non è possibile aggiungervi elementi, rimuoverli o modificarne alcuno.
"""
coordinate = (3.14, 2.71)
print(coordinate[0])
print(coordinate[1])

#estrazione dati da una tupla (unpacking)

name, age, city = ("Mari", 25, "Roma")
print(f"{name} ha {age} anni, e vive a {city}")

