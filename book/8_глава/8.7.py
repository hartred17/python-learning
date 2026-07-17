def make_album(artist_name, album_name, number_of_tracks=None):
    """Возвращает словарь с названием альбома и исполнителем."""
    album_dict = {'artist': artist_name, 'album': album_name, 'tracks': number_of_tracks}
    return album_dict 

album = make_album('ROCKET', 'Один')
print(album)

album = make_album('madk1d', 'sexyswag')
print(album)

album = make_album('Lil Skies', 'Life of a Dark Rose', 14)
print(album)
