from city_function import city_country

def test_cities():
    """Поддерживается ли формат вывода городов 'Santiago, Chile'?"""
    formated_city = city_country('santiago', 'chile')
    assert formated_city == 'Santiago, Chile'