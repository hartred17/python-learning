age = 65

if age < 2:
    status = "младенец"
elif age <  4:
    status = "малыш"
elif age < 13:
    status = "ребенок"
elif age < 20:
    status = "подросток"
elif age < 65:
    status = "взрослый"
else:
    status = "пожилой человек"

print(f"Вы {status}")
