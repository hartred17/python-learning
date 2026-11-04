def city_country(city, country, population=''):
    """Возвращает строку в формате: Город Страна - население xxx."""
    if population:
        full_city = f"{city.title()}, {country.title()} - population {population}"
        return full_city
    else:
        full_city = f"{city}, {country}"
        return full_city.title()