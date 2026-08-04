cities = {
    'moscow': {
        'country': 'russia',
        'population': '13.5 million',
        'fact': 'The Moscow Metro is over 500 km long.',
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'Tokyo was called Edo until 1868.',
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'The Louvre, one of the most visited museums in the world, is located in Paris.',
    },
}

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"  It's population - {population} people.")
    print(f"  {fact}")
