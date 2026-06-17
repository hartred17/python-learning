# Проверка равенства и неравенства строк
car = "bmw"
print(car == "bmw") #True
print(car == "audi") #False

# Проверка с lower()
name = "Alice"
print(name.lower() == "alice") #True
print(name.lower() == "bob") #False

# Числовые проверки
age = 18
print(age == 18) #True
print(age > 18) #False
print(age < 18) #False
print(age >= 18) #True
print(age <= 18) #True

# Проверки с and
print(age > 10 and age < 20) #True
print(age > 20 and age < 30) #False

# Проверки с or

print(age > 20 or age == 18) #True
print(age < 10 or age > 30) #False

# Проверка вхождения в список
fruits = ["apple", "banana"]
print("apple" in fruits) #True
print("orange" in fruits) #False

# Проверка отсутствия элемента в списке
print("orange" not in fruits) #True
print("banana" not in fruits) #False
