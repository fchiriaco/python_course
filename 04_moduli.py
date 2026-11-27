#importazione con alias
import datetime as dt
import math as m

today = dt.date.today()
td = str(today)

lista = td.split("-")
td_italia = lista[2] + "-" + lista[1] + "-" + lista[0]

print(td_italia)
print(m.pi)
