from datetime import datetime, timedelta, date

now = datetime.now()
print(now)
print(now.strftime("%d %B %Y"))
print(now.strftime("%Y-%m-%d %H:%M"))

yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(yesterday.strftime("%d %B %Y"))
print(next_week.strftime("%d %B %Y"))

birthday = date(1965, 6, 17)
today = date.today()
age_days = (today - birthday).days
print(f"Giorni passati da quando sono nato: {age_days:,}")
print("Evitiamo commenti inutili!!!!!!!!")
