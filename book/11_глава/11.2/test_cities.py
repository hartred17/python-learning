from city_function import city_country


def test_cities():
    """Поддерживается ли формат вывода городов 'Santiago, Chile'?"""
    formated_city = city_country("santiago", "chile")
    assert formated_city == "Santiago, Chile"


def test_city_country_population():
    """Поддерживает ли вывод в формате: 'Santiago, Chile - population xxx'."""
    formated_city = city_country("santiago", "chile", 5000000)
    assert formated_city == "Santiago, Chile - population 5000000"
