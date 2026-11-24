"""
I SET
Un set è una collezione non ordinata di valori unici. 
Non sono ammessi valori duplicati: se si tenta di aggiungere un valore già presente in un insieme, non accade nulla. 
Gli insiemi vengono definiti utilizzando le parentesi graffe, proprio come i dizionari, ma contengono valori anziché coppie chiave-valore.
"""

#Creare un set e rimuovere i duplicati
cities_with_duplicates = ["Roma", "Milano", "Roma", "Torino", "Genova", "Torino"]
unique_cities = set(cities_with_duplicates)
print(unique_cities)
print(len(unique_cities))

#operazioni
python_skills = {"variables", "loops", "functions", "classes"}
data_skills = {"functions", "pandas", "numpy", "classes"}
#Intersezione
print(python_skills & data_skills)
#unione
print(python_skills | data_skills)
#differenza e differenza simmetrica
print(python_skills - data_skills)
print(python_skills ^ data_skills)



