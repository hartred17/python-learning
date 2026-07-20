# Список моделей, которые необходимо напечатать.
unprinted_designs = ['phone case', 'robotpedant', 'dodecahedron']
completed_models = []

# Цикл последовательно печатает каждую можель до конца списка.
# После печати каждая можель перемещаетя в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
# Вывод готовых моделей.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
