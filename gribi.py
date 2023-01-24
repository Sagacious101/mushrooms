import random


name = "Вася Питонов"
mushrooms = 0
max_mushrooms = 100
spray = 20
max_spray = 20


while mushrooms < max_mushrooms and spray > 0:
	mushrooms_amount = random.randint(0, 100)
	mushrooms += mushrooms_amount
	spray -= 1
	if mushrooms > max_mushrooms:
		mushrooms = max_mushrooms
	space = max_mushrooms - mushrooms
	if mushrooms >= max_mushrooms:
		print("В корзине кончилось место!\n")
	if spray == 0:
		print("У вас кончился спрей")
	print(f"{name} ищет грибы...")
	print(f"Найдены грибы: {mushrooms_amount}")
	print(f"Оставшееся место в корзине: {space}")
	print(f"Корзина: {mushrooms}/{max_mushrooms}")
	print(f"Спрей: {spray}/{max_spray}\n")

