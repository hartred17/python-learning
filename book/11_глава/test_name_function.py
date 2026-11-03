from name_function import get_formatted_name

def test_first_last_name():
    """Поддерживаются ли имена типа 'Janis Joplin'?"""
    formatted_name = get_formatted_name('Janis', 'Joplin')
    assert formatted_name == 'Janis Joplin'