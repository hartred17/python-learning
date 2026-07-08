responses = {}

poling_active = True

while poling_active:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        poling_active = False
    
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}")
