favourite_languages = {
    "jen": "python", 
    "sarah": "c", 
    "edward": "rust", 
    "phil": "python",
    }

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite vanguage is {language.title()}")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
    if coder in favourite_languages:
        print(f"{coder.title()} спасибо за участие!")
    else:
        print(f"{coder.title()}, приглашаем вас пройти опрос ")
