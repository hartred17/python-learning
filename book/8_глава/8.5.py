def describe_city(city, country='russia'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('moscow')
describe_city(city='madrid', country='spain')
describe_city('berlin', 'germany')
