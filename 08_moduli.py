import random

print(random.randint(1, 100))

print(random.uniform(0.0, 1.0))

items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
print(random.choice(items))

sample = random.sample(items, 2)
print(sample)

random.shuffle(items)
print(items)