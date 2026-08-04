def make_car(manufacturer, model_name, **options):
    """Сохраняет данные об автомобиле в словаре."""
    car_dict = {
        'manufacturer': manufacturer,
        'model_name': model_name,
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

car = make_car('subaru', 'outback', color='blue', tow_packege=True)
print(car)
