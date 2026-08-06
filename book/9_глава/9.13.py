from random import randint

class Die:
    """Игра в кости."""

    def __init__(self, sides=6):
        """Инициализируем атрибуты sides"""
        self.sides = sides

    def roll_die(self):
        """Возвращает случайное число от 1 до кол-ва граней кубика."""
        return randint(1, self.sides)

# Создаем 6 гранный кубик и показываем резултат 10 бросков.
d6 = Die()

results = []

for roll in range(10):
    result = d6.roll_die()
    results.append(result)

print(f"Результаты 10 бросков 6 гранного кубика:")
print(results)

# Создаем 10 гранный кубик и показываем резултат 10 бросков.
d10 = Die(10)

results = []

for roll in range(10):
    result = d10.roll_die()
    results.append(result)

print(f"Результаты 10 бросков 10 гранного кубика:")
print(results)

# Создаем 20 гранный кубик и показываем резултат 10 бросков.
d20 = Die(20)

results = []

for roll in range(10):
    result = d20.roll_die()
    results.append(result)

print(f"Результаты 10 бросков 20 гранного кубика:")
print(results)
