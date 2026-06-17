# ============================
#  Python Crash Course — Глава 2
#  Практика строковых методов — решения
# ============================

# 1. Имя в разных регистрах
name = "ivan"
print(name.lower())   # ivan
print(name.upper())   # IVAN
print(name.title())   # Ivan


# 2. Форматированное приветствие
name = "Olga"
print(f"Hello, {name}, would you like to learn some Python today?")  


# 3. Удаление пробелов
name_with_spaces = "   Anna   "
print(name_with_spaces)            # "   Anna   "
print(name_with_spaces.lstrip())  # "Anna   "
print(name_with_spaces.rstrip())  # "   Anna"
print(name_with_spaces.strip())   # "Anna"


# 4. Работа с суффиксом
filename = "report.txt"
filename = filename.removesuffix('.txt')
print(f"{filename}.pdf")  # report.pdf


# 5. Изменение регистра цитаты
quote = "Life is what happens when you're busy making other plans."
print(quote.upper())  # Весь текст в верхнем регистре
print(quote.lower())  # Весь текст в нижнем регистре
print(quote.title())  # Заглавные буквы в начале каждого слова


# 6. Комбинирование методов
raw_name = "   aLiCe   "
raw_name = raw_name.strip()
raw_name = raw_name.lower()
print(f"Hello, {raw_name.title()}!")