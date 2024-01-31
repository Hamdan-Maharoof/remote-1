import random

cars = ["Toyota","Honda","Lexus"]

def model():
	return random.randrange(1980,2024)

print(random.choice(cars))
print(model())
