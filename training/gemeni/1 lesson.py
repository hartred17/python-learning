hero_name = "Тень"
health = 100
speed = 12.5
magic = True
health = health - 90
print(hero_name)
print(health)

if health <= 0:
    print("Game over")
else:
    print("Герой еще сражается!")
   