# Изначальный список
sities = ["Berlin", "Moscow", "Bangkok", "Hamburg"]
print(sities)
# Метод добавляет в конец списка
sities.append("Antalia")
print(sities)
# Метод добавляет в произвольную позицию списка
sities.insert(1, "Kazan")
print(sities)
# Оператор удаляет элемент из списка по индексу
del sities[1]
print(sities)
# Метод удаляет элемент из списка по индексу и позваляет работать с нима после удаления
poped_sity = sities.pop(1)
print(sities)
# Метод удаляет элемент по значению (удаляет только первое вхождение значения)
sities.remove("Berlin")
print(sities)
# Метод сортирует в алфавитном порядке (reverse=True в обратном)
sities.sort()
print(sities)
# Функция сортирует список в авфавитном но не меняет старый порядок (reverse=True в обратном)
sorted(sities)
print(sities)
# Метод изменяет порядок списка на обратный не алфавитный
sities.reverse()
print(sities)
# Функция выводит количество элементов списка
print(len(sities))
