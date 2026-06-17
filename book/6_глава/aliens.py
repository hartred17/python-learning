# Создание пустого списка для хранения данных о пришельцах.
aliens = []

#Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Вывод данных о первых 5 пришельцах:
for alien in aliens[:5]:
    print(alien)
print("...")

#Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")
